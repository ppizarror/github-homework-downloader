if (!String.format) {
    String.format = function(format) {
        var args = Array.prototype.slice.call(arguments, 1);
        return format.replace(/{(\d+)}/g, function(match, number) {
            return typeof args[number] != 'undefined' ?
                args[number] :
                match;
        });
    };
}

// Global vars
var timeout;

// If page is loaded
jQuery(document).ready(function($) {

    // Check all user id's
    $('#main_list > div').map(function() {
        cookie_status = Cookies.get(this.id);

        // If downloaded then display check button
        if (cookie_status != Cookies.undefined && this.id != '') {
            try {
                var json = JSON.parse(cookie_status);
                $(String.format('#{0} .user_inner .status img', this.id)).attr('src', 'res/check.png');
                $(String.format('#{0} .user_inner .status #status_date', this.id)).html(json.date_download);
            } catch (err) {}
        };

        // Listener to all download buttons
        if (this.id != '') {
            $(String.format('#{0} .user_inner #download', this.id)).click(function() {
                clicked_id = $(this).attr('user');
                $(String.format('#{0} .user_inner .status img', clicked_id)).attr('style', 'display: none');
                $(String.format('#{0} .user_inner .status #progress-bar-circle', clicked_id)).attr('style', 'display: block');
                var bar = new ProgressBar.Circle(String.format('#{0} .user_inner .status #progress-bar-circle', clicked_id), {
                    strokeWidth: 20,
                    easing: 'easeInOut',
                    duration: timewait_check,
                    color: '#3598DB',
                    trailColor: '#eee',
                    trailWidth: 1,
                    svgStyle: null
                });
                bar.animate(1);

                timeout = setTimeout(
                    function() {
                        Cookies.set(clicked_id, {
                            downloaded: true,
                            date_download: new Date().toLocaleString(),
                            path: ''
                        }, {
                            expires: 14
                        });
                        $(String.format('#{0} .user_inner .status #progress-bar-circle', clicked_id)).attr('style', 'display: none');
                        $(String.format('#{0} .user_inner .status img', clicked_id)).attr('src', 'res/check.png');
                        $(String.format('#{0} .user_inner .status img', clicked_id)).attr('style', 'display: block');
                        $(String.format('#{0} .user_inner .status #status_date', clicked_id)).html(new Date().toLocaleString());
                    }, timewait_check);
            });
        }
    });

    // Reset button
    $('#reset_button').click(function() {
        console.log('Reset download list');
        $('#main_list > div').map(function() {
            Cookies.remove(this.id);
        });
        location.reload();
    });
});
