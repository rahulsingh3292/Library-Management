function updateBook(csrf) {

  let book_name = $("#book_name").val();
  let author = $("#author").val();
  let category = $("#category_value").val();

  if (book_name == "") {
    $("#statusMsg").text("Plaese fill Book  Name");
    return
  }

  if (author == "") {
    $("#statusMsg").text("Plaese fill Book author Name");
    return
  }

  let bookData = {
    "csrfmiddlewaretoken": csrf,
    "book_name": book_name,
    "author": author,
    "category": category
  }
  let id = $("#book_update_id").val();
  $.ajax({
    url: `/library/update/${id}/`,
    method: "POST",
    data: bookData,
    success: function(resp) {
      $("#statusMsg").html('<p class="text-success text">Book updated successfully <i class="far fa-check ml-3"></i></p>');
      $("#search_results").html("")
      allBooks();
      document.getElementById('updatebookForm').reset();
      setTimeout(function() {
        $("#update_form").hide();
           $("#statusMsg").removeClass("text-success").addClass("text-info").text("update Books")
      }, 3000);
   
    }
  });
}

function searchBook() {
let book = $("#book_searched").val();
let id = $("#search_results").find(`option[value='${book}']`).first().text()

$.ajax({
url: `/library/search_book/`,
method: "GET",
data: {
"book_id": id
},
success: function(resp) {
if (resp["book"]) {
$("#update_form").show()
book = resp["book"]
$("#book_update_id").val(id);
$("#book_name").val(`${book["book_name"]}`)
$("#author").val(`${book["author"]}`);

$(".cat_options").each(function() {
if ($(this).attr("value") == book["cat_id"]) {
$(this).attr({
"selected": true
})

}

})


}

} // success function
})

}

function allBooks(){
  $.get("/library/books/",function(data){
    let books = data['books']
    for (let i=0; i<books.length; i++){
      
    $("#search_results").append(`  <option value="${books[i][0]}" class="opt_book"><p id="book_id">${books[i][1]}</p></option>`);
    }
  })
}