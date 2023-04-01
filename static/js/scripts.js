fetch("/get_my_ip")
	.then((res) => res.json())
	.then((data) => {
		document.querySelector("#test").innerText = data.ip;
	});
