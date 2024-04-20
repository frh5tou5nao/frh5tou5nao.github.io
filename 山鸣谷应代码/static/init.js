(function() {

	skel.init({
		reset: 'full',
		breakpoints: {
			'global': { range: '*', href: "/style.css", viewport: { scalable: false } },
			'normal': { range: '-1280', href: '/style-noscript.css' },
		}
	});

			window.onload = function() {
				document.body.className = '';
			}
			window.ontouchmove = function() {
				return false;
			}
			window.onorientationchange = function() {
				document.body.scrollTop = 0;
			}

})();