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
var homeworkname;
var msg_error_download = 'ERROR 404';
var timeoutlist = [];

// If page is loaded
jQuery(document).ready(function($) {

    // Get homework-name
    homeworkname = $('#homework_name').html();

    // Check all user id's
    $('#main_list > div').map(function() {
        cookie_status = Cookies.get(this.id + homeworkname);

        // Listener to all download buttons
        if (this.id != '') {
            $(String.format('#{0} .user_inner #download', this.id)).click(function(event) {
                clicked_id = $(this).attr('user');
                $(String.format('#{0} .user_inner .status img', clicked_id)).attr('style', 'display: none');
                $(String.format('#{0} .user_inner .status #status_date', clicked_id)).html('');
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
                        Cookies.remove(clicked_id + homeworkname);
                        Cookies.set(clicked_id + homeworkname, {
                            downloaded: true,
                            date_download: new Date().toLocaleString(),
                            homework: homeworkname
                        }, {
                            expires: 14
                        });
                        $(String.format('#{0} .user_inner .status #progress-bar-circle', clicked_id)).removeAttr('style');
                        $(String.format('#{0} .user_inner .status #progress-bar-circle', clicked_id)).html('');
                        $(String.format('#{0} .user_inner .status img', clicked_id)).attr('src', 'res/check.png');
                        $(String.format('#{0} .user_inner .status img', clicked_id)).removeAttr('style');
                        $(String.format('#{0} .user_inner .status #status_date', clicked_id)).html(new Date().toLocaleString());
                        for (var i = 0; i < timeoutlist.length; i++) {
                            if (timeoutlist[i][1] == clicked_id) {
                                timeoutlist.splice(i, i);
                                break;
                            }
                        }
                    }, timewait_check);
                timeoutlist.push([timeout, clicked_id]);
            });
        }

        // If downloaded then display check button
        if (cookie_status != Cookies.undefined && this.id != '') {
            try {
                var json = JSON.parse(cookie_status);
                if (json.homework == homeworkname) {
                    if (json.downloaded) {
                        $(String.format('#{0} .user_inner .status img', this.id)).attr('src', 'res/check.png');
                    }
                    $(String.format('#{0} .user_inner .status #status_date', this.id)).html(json.date_download);
                    if (json.date_download == msg_error_download) {
                        $(String.format('#{0}', this.id)).attr('class', 'error_download');
                        $(String.format('#{0} .user_inner #download', this.id)).unbind('click');
                        $(String.format('#{0} .user_inner #download', this.id)).removeAttr('href');
                        $(String.format('#{0} .user_inner #calendar', this.id)).removeAttr('href');
                        $(String.format('#{0} .user_inner #usernamelink', this.id)).removeAttr('href');
                    }
                }
            } catch (err) {}
        };
    });

    // Reset button
    $('#reset_button').click(function() {
        console.log('Reset download list');
        $('#main_list > div').map(function() {
            Cookies.remove(this.id + homeworkname);
        });
        location.reload();
    });

    // Scroll button
    var amountScrolled = 600;
    $(window).scroll(function() {
        location.pathname.replace(/^\//, '')
        if ($(window).scrollTop() > amountScrolled) {
            $('a.back-to-top').fadeIn('slow');
        } else {
            $('a.back-to-top').fadeOut('slow');
        }
    });
});

// Unload event cancel all timeouts
$(window).on("unload", function(e) {
    if (timeoutlist.length > 0) {
        console.log('Canceling all timeouts');
        for (var i = 0; i < timeoutlist.length; i++) {
            try {
                clearTimeout(timeoutlist[i][0]);
                Cookies.remove(timeoutlist[i][1] + homeworkname);
                Cookies.set(timeoutlist[i][1] + homeworkname, {
                    downloaded: false,
                    date_download: msg_error_download,
                    homework: homeworkname
                }, {
                    expires: 14
                });
            } catch (e) {} finally {}
        }
    }
});
