(function() {
    var _old_alert = window.alert;
    window.alert = function() {
                     // run some code when the alert pops up
        _old_alert.apply(window,arguments);
                     // run some code after the alert
        console.log("ACECTF{'this_is_an_easter_egg'}");
    };
})();
