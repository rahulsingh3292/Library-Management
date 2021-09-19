  $("#add_category").attr({
    "disabled": true
  })
  $("#category_title").keyup(function() {
    if (this.value == "") {
      $("#add_category").attr({
        "disabled": true
      })
    } else {
      $("#add_category").attr({
        "disabled": false
      })
    }
  })

function addCategory(csrf) {
    let title = $("#category_title").val();

    $.ajax({
      url: "/library/add_category/",
      method: "POST",
      data: {
        "csrfmiddlewaretoken": csrf,
        "title": title
      },
      success: function(resp) {
        $(".modal").modal("toggle")
        $("#category_value").append(`<option value="${resp["cat"][0]}" selected>${resp["cat"][1]}</option>`)
       
      }
    })

}


function addBook(csrf){
  let book_name = $("#book_name").val();
  let author = $("#author").val();
  let category = $("#category_value").val();
 
    if(book_name == ""){
     $("#statusMsg").text("Plaese fill Book  Name");
    return 
  }
  
  if (author == ""){
    $("#statusMsg").text("Plaese fill Book author Name");
    return 
  }
  

  let bookData ={"csrfmiddlewaretoken":csrf,"book_name":book_name,"author":author,"category":category}
  
  $.ajax({
    url : "/library/addbook/",
    method : "POST",
    data : bookData,
    success : function(resp){
      
      $("#statusMsg").html('<p class="text-success text">Book Added in Library <i class="far fa-check ml-3"></i></p>')
      document.getElementById('addbookForm').reset();
      setTimeout(function() {$("#statusMsg").html("").text("Add Books,category..")}, 2000);
    },
    error : function(err){
      console.log(err)
    }
  })
  
}

