//Project 01 Due: 4/22/2020  login.js

// This function uses REGEX to make sure the password is within the described parameters - at least 6 characters and one number
   function check_usrname(){ //checks username input
     var usrname_val=document.getElementById("usrname").value;
     var usrnameError=document.getElementById("usrnameError");
     //var usrname_val = str.replace(/</gi, "&lt"); // Prevents Cross-Site Scriptng
     if (usrname_val==""){ //if the field is empty:
       usrnameError.style.color = "red";
       usrnameError.innerHTML = "*Please enter a username";
       return false;
     }
     else{
       usrnameError.innerHTML = "";
       return true;
     }
   ////////////////////////////////////////////////////////////////////////
   function check_pwd(){ //validates password input
     // var pwd_pattern = new RegExp(/\w{6,}/);
     var pwd_pattern = new RegExp(/\w{6,}[0-9]{1,}/);
     var pwd_val = document.getElementById("pwd").value;
     //var pwd2_val = document.getElementById("pwd2").value;
     var test = pwd_pattern.test(pwd_val);
     var pwdError=document.getElementById("pwdError");
     //var pwd2Error=document.getElementById("pwd2Error");
     //var pwd_val = str.replace(/</gi. "&lt"); //Prevents Cross-Site Scripting
     // document.write(test)
     if (pwd_val==""){ //if the field is empty:
       pwdError.style.color = "red";
       pwdError.innerHTML = "*Please enter a password";
       return false;
    }
     if (test == false){ //if it does not match the regex:
       pwdError.style.color = "red";
       pwdError.innerHTML = "*Your password must be at least six characters and one number";
       return false;
     }
     /*if (pwd_val != pwd2_val){
        pwd2Error.style.color = "red";
        pwd2Error.innerHTML = "*Your password must match";
     }*/
     else{
       pwdError.innerHTML = "";
       //pwd2Error.innerHTML = "";
       return true;
      }
    }