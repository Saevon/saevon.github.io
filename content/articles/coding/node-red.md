Template: article
Title: Running Node-Red flows in the browser
Tagline: a convinient library can now run on the browser.
Date: 2016-08-09
Category: coding
Tags: node-red, javascript, browser


Node-Red is pretty useful for wiring together IOF (Internet of Things) devices, but its currently tied to node.js.
Here is a way to run it clientside (on a browser) for those things that aren't allowed to run node.js.


# Situation

I had devices that could only run JS through a chrome-like browser. Yet I needed a way to quickly deploy similar workflows to these devices. Each device would also act as a hub for other hardware on the system, this other hardware was easiest to connect through node-red.

Thus node-red didn't need any UI, but it did need a way to run the given flows on a browser.
The following needed to be done:

 * Add a route to get node-red configuration for this device
    * flows
    * credentials
 * Removing node-red's filesystem dependancy
 * Polyfilling any node.js modules node-red uses (that aren't browser compatible)


# Node-Red

!alert! info
    Checkout [my node-red repo][node-red-repo] to see the changes I had to make in node-red.
!endalert!

I didn't have to make too many changes to node-red itself to support this. I simply added a flag: `settings.noFileSystem`, and made sure any code that auto-loaded data from the filesystem on startup didn't get a chance to run if the flag was on. Thus in the browser, I would add this flag, but on the main node-red server, I would not.

(see the commit [here](https://github.com/Saevon/node-red/commit/0da7a1bb740a5aeaabbdfabf01c616f857c3f714#diff-555b375e1a6f534407fe74a7f1322bddR27))

!alert! warning
    None of this is release-ready yet, as there's a lot more to examine, add and test before any pull-request
!endalert!


Second, you can't set the active flow (since it's supposed to be loaded by the filesystem), so I needed a way to set that up too. This was quite easy as well.

```javascript
    // red/nodes/flows.js
    setActiveFlow: function(flow) {
        activeFlow = flow;
    },
```

Finally, there was a problem with the credentials requiring way too many

```javascript
var needsPermission = require("../api/auth").needsPermission;
```

While I was at it, I realize it would be nice to be able to use inject nodes in the browser as well, so I added an easy function to do so.
(see the commit [here](https://github.com/Saevon/node-red/commit/0f8bf91a75718a58517186c49a04732967554e6d))


```javascript
    // Usage:
    nodeRedInject('node-name');
```


# Browser Usage

To use node-red in the browser I needed to get the configuration, this basically means a bunch of flows to run.

Getting each flow was easy enough, added a route to the server, and do an Ajax call

```
/**
 * Gets a subflow
 *
 * @param flowId
 * @param callback
 * @returns subflow
 */
function getSubflow(flowId, callback) {
    jQuery.ajax('//' + window.location.hostname + '/subflow/' + flowId, {
        data: {},
    }).error(function(xhr) {
        return callback("Server Error: " + xhr.status + ". Can't get subflow(" + flowId + ")");
    }).done(function(subflow) {
        if (!_.isArray(subflow)) {
            return callback("Server Error: Invalid return");
        }
        return callback(null, subflow);
    });
}
```

Of course we can load more than one flow, so this waits for all the data to come back, and merges them all into one flow.

```
/**
 * Loads the given subflow Ids
 * @param flowIds
 */
function initSubflows(flowIds, callback) {
    var syncs = [];

    for (var i=0; i < flowIds.length; i++) {
        var flowId = flowIds[i];
        var defer = jQuery.Deferred();
        (function scope(defer, flowId) {
            getSubflow(flowId, function(err, subflow) {
                if (err) {
                    defer.resolve([]);
                    return console.error(err);
                }

                defer.resolve(subflow);
            });
        })(defer, flowId);

        syncs.push(defer.promise());
    }

    jQuery.when.apply(null, syncs).then(function() {
        var flowData = [];

        // Merge the subflows
        var args = Array.prototype.slice.call(arguments);
        for (var i in args) {
            flowData = flowData.concat(args[i]);
        }

        callback(null, flowData);
    });
}

```

Finally here is the way the entire thing is called. Note that the last callback is the one that loads the flows into node-red itself, starting it.

```javascript
    // Load the flows that we need
    var flowIds = params.flows;
    if (flowIds) {
        flowIds = flowIds.split(",");
        initSubflows(flowIds,  function onSubflowData(err, flowData) {
            RED.loadFlowData(flowData);
        });
    }
```


##




# Reference

* [My Node-Red Repo][node-red-repo]

[node-red-repo]: https://github.com/Saevon/node-red/

