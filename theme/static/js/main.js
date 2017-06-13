$(function onLoad() {
    if (!enable_history) {
        // We don't always want to do this
        return;
    }

    var referrer = document.referrer;
    var site = referrer.match(new RegExp(location.host + '/?(.*)'));
    if (!site) {
        // Outside link, use defaults
        return;
    }

    var path = site[1];

    console.log(path)

    // Inside link!
    var title = history_mapping[path];
    if (!title) {
        // If we can't figure out the proper link/title
        // Give up and use defaults
        return;
    }

    // Link each one to the expected URL
    $('.back-link').each(function() {
        // Make each back link go in history
        this.href = 'javascript: history.back()';
    });

    // Update the title
    $('.back-link-name').each(function() {
        $(this).text('to "' + title + '"');
    });
});

