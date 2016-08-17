$(function onLoad() {
    $('a.back-link').each(function(elem) {
        this.href = document.referrer;
    });
});

