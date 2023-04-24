//
//$(document).ready(function() {
//
////$( "#submit" ).click(function(el) {
////  alert( "Handler for .click() called." );
////  url = compute_url(1);
//////  window.location.redirect(url);
////  location.replace(url);
////});
//
//$( ".pageno" ).click(function(el) {
////    $( "#submit" ).click();
//  var pageno = el.currentTarget.innerText;
//  url = compute_url(pageno);
////  window.location.redirect(url);
////  window.location.replace(url);
//  location.replace(url);
//  $.get(url, function(data, status){
//        alert("Data: " + data + "\nStatus: " + status);
//    });
//});
//
//function compute_url(pageno=1){
//    url = 'localhost:8000/accounts/search/?';
//
//  if (!pageno)
//        {
//        pageno=1;
//        }
//  url += 'page='+ pageno +'&';
//  search_string = $( "#search-text" )[0].value;
//  search_by = $( "#search-by" )[0].value;
//  if(search_by && search_string){
//    if(search_by=="Search By child Patient"){url +='patient='+search_string;}
//    else if(search_by=="Search By Pincode"){url += 'pincode='+search_string;}
//    else if(search_by=="Search By Doctor"){url += 'doctor='+search_string;}
//  }
//  console.log(url);
//  return url;
//}
//
//
//});
