---
layout: post
title: "WebRTC with JsSIP and Asterisk"
date: 2013-07-03
description: "Trying to get leading edge tech to work: WebRTC"
category: Case-Studies
tags: [webrtc, jssip, asterisk]
---
{% include JB/setup %}

Recently I've been trying to get a web phone up and running, my only real requirement was to use asterisk.


## Browsers

I've only tried to use chrome so far, though I've read that Firefox is currently WebRTC capable as well.

Chrome on OSX seems to work fine (version 27.0.1453.116).
Chrome on Ubuntu had problems until I updated to a [Beta version](http://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-beta) (version 28.0.1500.52 beta)

## Asterisk

Asterisk had quite a few requirements before I could get it to work with WebRTC, [see this page for details](https://wiki.asterisk.org/wiki/display/AST/Asterisk+WebRTC+Support).

#### Building

You will likely need to rebuild Asterisk as WebRTC requires a SRTP libraries, which aren't included by default.

You will need the following libraries on the machine you use to recompile Asterisk:

  - libssl-dev
  - libsrtp0

Once you have these libraries installed, you will also need to enable two Asterisk resources:

  - res_srtp.so
  - res_http_websocket.so

Now you can recompile.

The resulting build might also need a few configuration changes:

    /etc/asterisk/
      |-- http.conf
      |-- modules.conf
      |-- sip.conf

- **http.conf**
    - enabled=yes
    - bindaddr=0.0.0.0
    - bindport=8088
- **modules.conf**
    you must load res_http_websocket.so before chan_sip.so
- **sip.conf**
    Any users that you want to allow WebRTC for you need:

        - encryption=yes
        - avpf=yes
        - transport=ws,wss
        - icesupport=yes

    Adding **encryption=yes** to any non WebRTC phones might make them break, so be careful.

Remember to restart Asterisk once you're done.

## JsSIP

JsSIP [JsSIP](http://jssip.net/) was quite easy to use, however it wasn't without its set of problems. If you want to do a quick test yourself, check out the [JsSIP Tryit](jssip.tryit.net) page.

My main problem was that their script didn't seem to connect with asterisk properly, though I've already forgotten the reason (will update if I do). To solve this I updated to the dev version of JsSIP, which I download from the [JsSIP Tryit](jssip.tryit.net) page.

Afterwards I would also have jssip error out when I tried to type in an invalid target, I patched it quickly removing the potentially erroneous code. I didn't know enough about their side of the problem, so I have no way of knowing if this is a correct fix.

I've included the patch below, use it at your own risk.


{% hightlight diff %}

Index: /static/js/jssip-devel.js
===================================================================
--- /static/js/jssip-devel.js
+++ /static/js/jssip-devel.js
@@ -3372,5 +3372,10 @@
         console.log(LOG_PREFIX +'ICE candidate received: '+ e.candidate.candidate);
       } else {
-        self.onIceCompleted();
+       // PATCH: (saevon) Fixes bug with the code crashing at this step.
+       // since: neither createOffer nor createAnswer get called if you
+       // had an "Invalid Target"
+       // Thus the method doesn't get added yet
+       if (self.onIceCompleted) {
+           self.onIceCompleted();
+       }
       }
     };

{% endhighlight %}


#### One-Way Audio

There was one unexpected problem that seems to have been causing one way audio for me.

When the **call_start** event fires you have a few methods you can use to get the local and remote streams, which would be quite useful for video, except I wasn't using video at the time. So I ended up ignoring these callbacks.

Unexpectedly the only way to get sound back was in fact throught the remote stream, which I would then attach to a video tag on my html page.


{% highlight javascript %}

call.on('started', function(event) {
    if (call.getRemoteStreams().length > 0) {
        var remoteView = document.getElementById('remoteView');
        remoteView.src = window.URL.createObjectUrl(
            call.getRemoteStreams()[0]
        );
    }
});

{% endhighlight %}


## Conclusion

WebRTC is clearly still a work in progress, and I hope it gets polished up nicely for when I net wish to use it.


