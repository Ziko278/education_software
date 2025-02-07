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

  

// next button function
$(document).on('click','.uploads-next', function() {
  
  checker_extension = $(this).attr("id-modifier")
  missing = $("#requirement-"+ checker_extension).text()

  if(checker_extension == ""){
    $('.overseas-page').hide()
    $('#overseas-page-1').show();
    $('#review-attachment').hide();

    $('.admission-process').removeClass("disabled-upload-link");
    $('#name').val("");
    $('#email').val("");
    $('#number').val("");
    $('#date').val("");
    // iteration to clear all the input fields
    for (i=1; i <=9; i++){

      $("#item-uploaded-" + i).val("")
    }

    if($(this).attr('response') == "form-submitted"){
      

      alert("submitted")
    }
    
    } else if(checker_extension == "9"){
      
        
      $(this).parents('.uploads-content').hide();
      $(this).parents('.uploads-content').next('.uploads-content').show(); 
      submitted_name = $('#name').val();
      submitted_email = $('#email').val();
      submitted_phone = $('#number').val();
      submitted_date = $('#date').val();
      
      $('#submitted-name').text(submitted_name);
      $('#submitted-email').text(submitted_email);
      $('#submitted-phone').text(submitted_phone);
      $('#submitted-date').text(submitted_date);


  } else{
    if($("#item-uploaded-"+checker_extension).val()==""){
      
        
      alert("Please, upload "+ missing )
    } else{
                    // Go to the next  element
                    $(this).parents('.uploads-content').hide();
                    $(this).parents('.uploads-content').next('.uploads-content').show(); 

    }
  }
});




// exit applicant details and show the upload section
$('#load-uploads').click(function() {
  $('#overseas-page-5').show();
  $('#overseas-page-4').hide();
  $('#upload-1').show();
  $('.uploads-navigation-b').hide();

});

//  exit the upload section and return to applicant details
$('#close-uploads').click(function() {
  $('.uploads-content').hide();
  $('#overseas-page-5').hide();
  $('#overseas-page-4').show();
});

  
$('.admission-process').click(function() {

  let section_reference =  $(this).attr("id-modifier");
  
  $('.overseas-page').hide()
  $("#overseas-page-"+ section_reference).show();
  if(section_reference == "4"){

      $('.admission-process').addClass("disabled-upload-link");
  }



  });



  // show the remove button when a file is attached
  $(".placement-attachment").change(function(){
    extension = $(this).attr("id-modifier")
    
    if($(this).val() ==""){
      $("#delete-placement-attachment-"+ extension).hide()
      // $("#upload-icon-"+ extension).removeClass("fa-check").addClass("fa-x")
      
    } else {
      $("#delete-placement-attachment-"+ extension).show()
      // $("#upload-icon-"+ extension).removeClass("fa-x").addClass("fa-check")
      
    }
    
  })


  // delete uploaded item and hide the remove button 
  $(".delete-placement-attachment").click(function(){
    delete_extension = $(this).attr("id-modifier")
    $("#placement-attachment-"+ delete_extension).val("")
    // $("#attachment-"+delete_extension ).text("No file attached")   
    $(this).hide()
    // $("#upload-icon-"+ delete_extension).removeClass("fa-check").addClass("fa-x")
    
  })


  // // show the remove button when a file is attached
  // $(".uploads-input").change(function(){
  //   extension = $(this).attr("id-modifier")
    
  //   if($(this).val() ==""){
  //     $("#delete-item-uploaded-"+ extension).hide()
  //     $("#upload-icon-"+ extension).removeClass("fa-check").addClass("fa-x")
      
  //   } else {
  //     $("#delete-item-uploaded-"+ extension).show()
  //     $("#upload-icon-"+ extension).removeClass("fa-x").addClass("fa-check")
      
  //   }
    
  // })

  

  // delete uploaded item and hide the remove button 
  $(".delete-item-uploaded").click(function(){
    delete_extension = $(this).attr("id-modifier")
    $("#item-uploaded-"+ delete_extension).val("")
    // $("#attachment-"+delete_extension ).text("No file attached")   
    $(this).hide()
    // $("#upload-icon-"+ delete_extension).removeClass("fa-check").addClass("fa-x")
    
  })



  
  // delete uploaded item and hide the remove button 
  // $(".delete-item-uploaded").click(function(){
  //   delete_extension = $(this).attr("id-modifier")
  //   $("#item-uploaded-"+ delete_extension).val("")
  //   $("#attachment-"+delete_extension ).text("No file attached")   
  //   $(this).hide()
  //   $("#upload-icon-"+ delete_extension).removeClass("fa-check").addClass("fa-x")
    
  // })

  // close the review page and return to the target upload page 
  $(".attachment-link").click(function(){
    upload_extension = $(this).attr('id-modifier')
    $("#upload-" + upload_extension).show()
    $(".uploads-navigation-b").show()
    $(".uploads-navigation").hide()
    $("#review-attachment").hide()
  })
  
  
  $(".show-uploads-page").click(function(){
    $(".overseas-page").hide()
    $("#overseas-page-3").show()
    $("html, body").animate({
      scrollTop: $("#placement-name").offset().top
    },1000, "easeInOutExpo");

    
  })

  
    // return the review page and close the active upload page 
  // $(".show-review-page").click(function(){
  //   active_page_extension = $(this).attr('id-modifier')
  //   $("#upload-"+ active_page_extension).hide() 
  //   $(".uploads-navigation-b").hide()
  //   $(".uploads-navigation").show()
  //   $("#review-attachment").show()
  // })
  

  // need to make this work so it does not stop the last optional loading in the event it is empty
    // return the review page and close the active upload page 
  $(".show-review-page").click(function(){

    active_page_extension = $(this).attr('id-modifier')
    missing = $("#requirement-"+ active_page_extension).text()

    if(active_page_extension =="9"){
      $("#upload-"+ active_page_extension).hide() 
      $(".uploads-navigation-b").hide()
      $(".uploads-navigation").show()
      $("#review-attachment").show()
    } else if($("#item-uploaded-"+active_page_extension).val()==""){
        alert("Please, upload "+ missing )
      } else {
        $("#upload-"+ active_page_extension).hide() 
        $(".uploads-navigation-b").hide()
        $(".uploads-navigation").show()
        $("#review-attachment").show()

      }
        
  })
 
})

