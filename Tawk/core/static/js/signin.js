newFunction();
function newFunction() {
  var form_fields = document.getElementsByTagName("input");
  //console.log(form_fields)
  //form_fields[1].placeholder='Username..';
  form_fields[1].placeholder = "Username..";
  form_fields[2].placeholder = "Enter password...";
  //form_fields[3].placeholder = "Re-enter Password...";

  //form_fields[1].className += 'input is-medium'
  form_fields[1].className += "input is-medium";
  form_fields[2].className += "input is-medium";
  //form_fields[3].className += "input is-medium";
}
