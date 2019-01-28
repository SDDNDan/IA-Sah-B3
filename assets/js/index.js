// This function will run a throttled script every 300 ms
var checkHeader = _.throttle(() => {
    // Detect scroll position
    let scrollPosition = Math.round(window.scrollY);

    // If we've scrolled 100px, add "sticky" class to the header
    if (scrollPosition > 100) {
        document.querySelector('header').classList.add('sticky');
    }

    else // If not, remove "sticky" class from header
    {
        document.querySelector('header').classList.remove('sticky');
    }
}, 10);

// Run the checkHeader function every time you scroll
window.addEventListener('scroll', checkHeader);