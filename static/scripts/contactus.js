let flag = 1; //1 is for not error  and 0 is for error
const specialChars = `(?=.*[!@#$%^&*\/])`;
function validName(elem) {
  if (elem.value.trim() <= 0) {
    document.querySelector("#nameError").innerText = "Name is required";
    flag = 0;
  } else {
    if (!isNaN(elem.value)) {
      document.querySelector("#nameError").innerText =
        "Name must start with letter";
      flag = 0;
    } else {
      if (
        elem.value.match(`(?=.*[!@#$%^&*\/])`) ||
        elem.value.match(`(?=.*[0-9])`)
      ) {
        document.querySelector("#nameError").innerText =
          "Name must not have special characters and Numbers";
        flag = 0;
      } else {
        if (!elem.value.match(/^[a-zA-Z]+ [a-zA-Z]+$/)) {
          document.querySelector("#nameError").innerText =
            "Name Must Have First Name and Last Name";
          flag = 0;
        } else {
          document.querySelector("#nameError").innerText = "";
          flag = 1;
        }
      }
    }
  }
}
function validPhone(elem) {
  if (elem.value.trim() <= 0) {
    document.querySelector("#phoneError").innerText = "Please fill your number";
    flag = 0;
  } else {
    if (isNaN(elem.value)) {
      document.querySelector("#phoneError").innerText =
        "Only supported numbers";
      flag = 0;
    } else if (elem.value.length < 10) {
      document.querySelector("#phoneError").innerText =
        "Number must be 10 digits";
      flag = 0;
    } else {
      if (elem.value.length > 10) {
        document.querySelector("#phoneError").innerText =
          "Number must be 10 digits";
        flag = 0;
      } else {
        if ((elem.value.length = 10)) {
          document.querySelector("#phoneError").innerText = "";
          flag = 1;
        } else {
          document.querySelector("#phoneError").innerText = "";
          flag = 1;
        }
      }
    }
  }
}

function validMessage(elem) {
  if (elem.value.trim() <= 0) {
    document.querySelector("#contentError").innerText = "Write something";
    flag = 0;
  } else {
    if (!isNaN(elem.value)) {
      document.querySelector("#contentError").innerText =
        "Must contain alfabets";
      flag = 0;
    } else {
      if (elem.value.length < 15) {
        document.querySelector("#contentError").innerText =
          "Must contain 15 characters";
        flag = 0;
      } else {
        document.querySelector("#contentError").innerText = "";
        flag = 1;
      }
    }
  }
}
function validate() {
  if (flag == 1) {
    return true;
  } else {
    return false;
  }
}

//
document.querySelector("#phone").value = "";
document.querySelector("#name").value = "";
