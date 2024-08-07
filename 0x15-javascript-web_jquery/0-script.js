const script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.2.1.min.js';
script.defer = true;
document.head.appendChild(script);

script.onload = function () {
	const header = document.querySelector('header');
	if (header) {
		header.style.color = '#FF0000';
	}
};
