myList = ["Jack", "Jill", "Beany", "Giant", "Goose"];

function showList() {
	let dataList = "<ul>";
	for (let name in myList) {
		dataList += "<li>" + myList[name] + "</li>";
	}

	dataList += "</ul>";

	document.getElementById("btnText").innerHTML = dataList;
}

function hideList() {
	document.getElementById("btnText").innerHTML = "";
}
