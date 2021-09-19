$("#signup").attr({"disabled":true})
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function button(type){
  if (type == "enable"){
    $("#signup").attr({"disabled":false})
  } else {
       $("#signup").attr({"disabled":true})
  }
}

$("#email").keyup(function(){
  if(validateEmail(this.value)){
    button("enable");
    $(this).addClass("text-success").removeClass("text-danger")
  } else{
    button("disable");
    $(this).removeClass("text-sucess").addClass("text-danger")
  }
})

$("#c_pass").keyup(function(){
  if ($(this).val() != $("#password").val() ){
    button("disable")
    $(this).addClass("text-danger").removeClass("text-success")
  } else{
    button("enable")
      $(this).addClass("text-success").removeClass("text-danger")
  }
})


$("#signup").click(function(){
  let first_name = $("#name").val();
  let email = $("#email").val();
  let password = $("#password").val();
  let ac_type = $("#acType").val();
  let csrf = $("input[name='csrfmiddlewaretoken']").val();
   
   
    if (ac_type == "chooseAc"){
      
    $("#statusMsgs").text("Plaese Select Account Type..")
    return 
  }
  
  if(first_name == ""){
 
     $("#statusMsgs").text("Enter you name ")
    return
  }
  

    
  if (password == ""){
     $("#statusMsgs").text("password Cannot be blank..")
    return 
  }
  
  if(password.length < 5){
     $("#statusMsgs").text("password length should be more than 5 characters.")
    return 
  }
 
 if ($("#c_pass").val() != password){
    $("#statusMsgs").text("password not matched..")
   return 
 }
  
 let signupData = {"first_name":first_name,"email":email,"password":password,"csrfmiddlewaretoken":csrf,"ac_type":ac_type}
  $("#statusMsgs").removeClass("alert-danger").addClass("alert-info").text("Plaese wait...")
  $.ajax({
    url : "/accounts/signup/",
    method : "POST",
    data : signupData,
    success : function(resp){
      
      if(resp["status"]) {
          $("#statusMsgs").removeClass("alert-danger alert-info").addClass("alert-success").text("Account is Created please Check your Email for Activate your account.. redirecting to login page..")
          document.getElementById("signupForm").reset();
        setTimeout(function (){
          window.location.replace("/accounts/login/")
        },3000)
      } else{
        $("#statusMsgs").text("This Email already Exists")
      }
    } // Success function ends here..
  })
  
})