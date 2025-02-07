$(document).ready(function() {

  flags = [
'australia.png',
'austria.png',
'belgium.png',
'canada.png',
'china.png',
'cyprus.png',
'denmark.png',
'finland.png',
'france.png',
'germany.png',
'hungary.png',
'india.jpeg',
'ireland.png',
'italy.png',
'lithuania.png',
'malaysia.png',
'malta.png',
'mauritius.png',
'monaco.png',
'netherland.png',
'new zealand.png',
'poland.png',
'russia.png',
'singapore.png',
// 'south korea.jpeg',
'south korea.png',
'spain.png',
'sweden.png',
'switzerland.png',
'uae.png',
'uk.png',
'us.png'

  ]
  flagImages = ""
  for(flag in flags){
    flagImages +=`<img src="/static/website/images/Study Abroad/Flags/${flags[flag]}" alt="${flags[flag]}">`
    $(".country-flags").html(flagImages)
// alert()
  } 


  // Click event for product images
  $('.post-item').click(function() {
    // Get the clicked image source
    var clickedImageSrc = $(this).find('img').attr('src');
    
    // Get the text of the clicked product (the title)
    var clickedTitle = $(this).find('.content a').text();
    
    // Get the current active image src and title
    var activeImageSrc = $('#main-image').attr('src');
    var activeTitle = $('#main-title').text();

    // Swap the image sources
    $(this).find('img').attr('src', activeImageSrc);
    $('#main-image').attr('src', clickedImageSrc);

    // Swap the text content
    $(this).find('.content a').text(activeTitle);
    $('#main-title').text(clickedTitle);
    
    $('.overseas-page').hide();
    $('#overseas-page-1').show();
    
  });
  
  $('.show-uploads-page').click(function() {
  // $('#request-review-btn').click(function() {
    $('#placement-country').val();
    var countryPhrase = $('#main-title').text();
    if ($(this).attr("page") == "flier"){
          var chosenCountry = countryPhrase.split("in ")[1];
    $('#placement-country').val(chosenCountry);
    }

    $('.overseas-page').hide();
    $('#overseas-page-3').show();
    });
});

