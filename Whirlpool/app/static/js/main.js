function validateForm() {
  var x = document.forms["add"]["title"].value;
  var y = document.forms["add"]["date"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }

  if (y == "") {
  	alert("Date must be filled out");
  	return false;
  }
}