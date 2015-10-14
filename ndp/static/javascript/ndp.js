for (var a = [], i = 0; i < 13; ++i)
    a[i] = i + 1;
function shuffle(array) {
    var tmp, current, top = array.length;
    if (top)
        while (--top) {
            current = Math.floor(Math.random() * (top + 1));
            tmp = array[current];
            array[current] = array[top];
            array[top] = tmp;
        }
    return array;
}
a = shuffle(a);
$(document).ready(function () {
    var i = 0;
    $(".home .sector-bubble").each(function () {
        $(this).addClass("sectorPos" + a[i]);
        $(this).delay(i * 500).queue(function (next) {
            $(this).addClass("pulse");
            $(this).trigger('hover');
            next();
        });
        i++;
    });
    assign_bootstrap_mode();
    shortenText();
    $(window).resize(function () {
        assign_bootstrap_mode();

    });
    $('.home .sector-bubble').each(function () {
        var blurb = $('.blurb', this).html();
        console.log(blurb);
        $(this).tipso({
            speed: 400,
            background: '#fae9bd',
            color: '#000000',
            titleColor: '#000000',
            showArrow: true,
            position: 'top',
            width: 200,
            maxWidth: '',
            delay: 200,
            animationIn: 'flipInY',
            animationOut: 'flipOutY',
            offsetX: 0,
            offsetY: 0,
            tooltipHover: true,
            content: blurb
        });
    });
    $('.sector-links ul').randomize('li');
});
$.fn.randomize = function (selector) {
    var $elems = selector ? $(this).find(selector) : $(this).children(),
            $parents = $elems.parent();
    $parents.each(function () {
        $(this).children(selector).sort(function () {
            return Math.round(Math.random()) - 0.5;
        }).detach().appendTo(this);
    });
    return this;
};
function assign_bootstrap_mode() {
    width = $(window).width();
    var mode = '';
    if (width < 768) {
        mode = "mode-xs";
    } else if (width < 992) {
        mode = "mode-sm";
    } else if (width < 1200) {
        mode = "mode-md";
    } else if (width > 1200) {
        mode = "mode-lg";
    }
    $("body").removeClass("mode-xs").removeClass("mode-sm").removeClass("mode-md").removeClass("mode-lg").addClass(mode);
}

function shortenText() {
    $('.contributors').readmore({
        speed: 75,
        collapsedHeight: 210,
        lessLink: '<p class="more-less"><a href="#">SHOW LESS</a></p>',
        moreLink: '<p class="more-less"><a href="#">SHOW MORE</a></p>'
    });

    if ($('body').is('.mode-xs') || $('body').is('.mode-sm')) {
        $('.vision, .goals').readmore({
            speed: 75,
            lessLink: '<p class="more-less"><a href="#">READ LESS</a></p>',
            moreLink: '<p class="more-less"><a href="#">READ MORE</a></p>'
        });
    }
}

$(function() {
  var url = 'http://' + window.location.hostname;
  var tweet = 'Demystifying and tracking the progress of the National Development Plan #NDP2030';

  // social buttons
  $('.fb-share').on('click', function(e) {
    e.preventDefault();

    window.open("https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(url),
                "share", "width=600, height=400, scrollbars=no");
    ga('send', 'social', 'facebook', 'share', url);
  });

  $('.twitter-share').on('click', function(e) {
    e.preventDefault();

    window.open("https://twitter.com/intent/tweet?" +
                "text=" + encodeURIComponent(tweet) +
                "&url=" + encodeURIComponent(url) +
                "share", "width=364, height=250, scrollbars=no");
    ga('send', 'social', 'twitter', 'share', url);
  });
});
