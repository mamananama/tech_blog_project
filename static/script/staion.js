const $route_status = document.querySelectorAll(".col-3");

Array.prototype.forEach.call($route_status, (content) => {
	if (content.innerText == "운행 전") {
		content.style.color = "orange";
	} else if (content.innerText == "운행 중") {
		content.style.color = "green";
	} else {
		content.style.color = "black";
	}
});
