/*---------- Mobile-Navbar Nav Toggler ----------*/

$(document).ready(function(){

  $(".nav-link > .main-nav-link").click(function() {
    // Close all main-nav-links in sibling nav-links
    $(this).closest('.nav-link').siblings().find('.main-nav-link').removeClass("active").next(".sub-nav-link").removeClass("active").slideUp();
    // Update icons to "fa-plus" for all main-nav-links in sibling nav-links
    $(this).closest('.nav-link').siblings().find('.main-nav-link i').removeClass("fa-minus").addClass("fa-plus");
  
    // Toggle "active" class for the clicked main-nav-link
    $(this).toggleClass("active");
    // Toggle slide for the corresponding sub-navigation
    $(this).next(".sub-nav-link").toggleClass("active").slideToggle();
    // Toggle icon class for the clicked main-nav-link
    $(this).find("i").toggleClass("fa-minus fa-plus");
    
  });
  
  $(".states-list > .main-states-list").click(function() {
    // Close all main-states-lists in sibling states-lists
    $(this).closest('.states-list').siblings().find('.main-states-list').removeClass("active").next(".sub-states-list").removeClass("active").slideUp();
    // Update icons to "fa-plus" for all main-states-lists in sibling states-lists
    $(this).closest('.states-list').siblings().find('.main-states-list i').removeClass("fa-minus").addClass("fa-plus");
  
    // Toggle "active" class for the clicked main-states-list
    $(this).toggleClass("active");
    // Toggle slide for the corresponding sub-navigation
    $(this).next(".sub-states-list").toggleClass("active").slideToggle();
    // Toggle icon class for the clicked main-states-list
    $(this).find("i").toggleClass("fa-minus fa-plus");
    
  });
  
  $(".examinations-list > .main-examinations-list").click(function() {
    // Close all main-states-lists in sibling states-lists
    $(this).closest('.examinations-list').siblings().find('.main-examinations-list').removeClass("active").next(".sub-examinations-list").removeClass("active").slideUp();
    // Update icons to "fa-plus" for all main-states-lists in sibling states-lists
    $(this).closest('.examinations-list').siblings().find('.main-examinations-list i').removeClass("fa-minus").addClass("fa-plus");
  
    // Toggle "active" class for the clicked main-states-list
    $(this).toggleClass("active");
    // Toggle slide for the corresponding sub-navigation
    $(this).next(".sub-examinations-list").toggleClass("active").slideToggle();
    // Toggle icon class for the clicked main-states-list
    $(this).find("i").toggleClass("fa-minus fa-plus");
    
  });
  
    $(".uploads-headings").click(function() {
    // Toggle "active" class for the clicked main-states-list
    $(this).toggleClass("active");
    // Toggle slide for the corresponding sub-navigation
    $(".hulled").toggle();
    $(".uploads-content").hide();
    $("#frees").show();
    // $(this).next(".sub-states-list").toggleClass("active").slideToggle();
    // Toggle icon class for the clicked main-states-list
    $(this).find("i").toggleClass("fa-minus fa-plus");
  });

  
    $(".overseas-content").click(function() {
      
      $(".overseas-content-description").slideUp("slow");
      $(this).nextUntil(".overseas-content").slideDown("slow");
      $(this).find("i").toggleClass("fa-minus fa-plus");
      $(".overseas-content").find("i").removeClass("fa-minus").addClass("fa-plus");
      $(this).find("i").addClass("fa-minus").removeClass("fa-plus");

  });

}); 
