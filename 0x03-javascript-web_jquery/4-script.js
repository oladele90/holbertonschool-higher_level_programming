$('toggle_header').click(function() {
    if ($('#header').hasClass('green')) {
        $('#header').toggleClass('red')
        $('#header').removeClass('green')
    } else {
        $('#header').toggleClass('green')
        $('#header').removeClass('red')
    }
})