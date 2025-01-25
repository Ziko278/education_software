/*---------- uploads ----------*/
// Document ready function to ensure the script runs after the DOM is fully loaded.
$(document).ready(function(){

  // Click event handler for the uploads.
  $(".uploads-heading").click(function(){

    // Check if the clicked uploads is already active.
    if($(this).hasClass("active")){
      // If active, close the uploads by removing active class and changing the icon.
      $(this).removeClass("active");
      $(this).find("i").removeClass("fa-minus").addClass("fa-plus");
      $(".uploads-content").hide();
    }

    else{
      // If not active, close any open uploads and open the clicked one.
      $(".uploads").removeClass("active");
      $(".uploads .uploads-heading i").removeClass("fa-minus").addClass("fa-plus");
      $(this).addClass("active");
      $(this).find("i").removeClass("fa-plus").addClass("fa-minus");
      $(".uploads-content").show();
      
    }
  })


  
  // Back button functionality
  $(document).on('click','.uploads-back', function() {
  // Go back to the previous element
  $(this).parents('.uploads-content').prev('.uploads-content').show();
  $(this).parents('.uploads-content').hide();
});
  
  // Next button functionality
$(document).on('click','.uploads-next', function() {
  // Go to the next  element
  $(this).parents('.uploads-content').hide();
  $(this).parents('.uploads-content').next('.uploads-content').show();
});

// additional functionality for the last "Next" button
$('#load-applicant-details').click(function() {
  submitted_name = $('#name').val();
  submitted_email = $('#email').val();
  submitted_phone = $('#number').val();
  submitted_date = $('#date').val();
 
   $('#submitted-name').text(submitted_name);
   $('#submitted-email').text(submitted_email);
   $('#submitted-phone').text(submitted_phone);
   $('#submitted-date').text(submitted_date);

 
});


// exit applicant details and show the upload section
$('#load-uploads').click(function() {
  $('#overseas-page5').show();
  $('#overseas-page4').hide();
  $('#first-upload').show();
  $('.uploads-navigation-b').hide();


});

//  exit the upload section and return to applicant details
$('#close-uploads').click(function() {
  $('.uploads-content').hide();
  $('#overseas-page5').hide();
  $('#overseas-page4').show();
});

  
$('.admission-process').click(function() {

  let section_reference =  $(this).attr("id-holder");
  
  $('.overseas-page').hide()
  $('#'+ section_reference).show();


  });

  // show the remove button when a file is attached
  $(".uploads-input").change(function(){
    target_button = $(this).attr("id-holder")
    if($(this).val() ==""){
      $("#"+target_button).hide()
    } else {
            $("#"+target_button).show()

    }
  })


  // delete uploaded item and hide the remove button 
  $(".delete-item-uploaded").click(function(){
        target_input = $(this).attr("id-holder")
      $("#"+target_input).val("")
      $(this).hide()
  })

  // close the review page and return to the target upload page 
  $(".attachment-link").click(function(){
    target_upload_page = $(this).attr('id-holder')
    $("#"+target_upload_page).show()
    $(".uploads-navigation-b").show()
    $(".uploads-navigation").hide()
    $("#review-attachment").hide()
  })

  
    // return the review page and close the active upload page 
  $(".show-review-page").click(function(){
    active_upload_page = $(this).attr('id-holder')
    $("#"+ active_upload_page).hide() 
    $(".uploads-navigation-b").hide()
    $(".uploads-navigation").show()
    $("#review-attachment").show()
  })

  




})