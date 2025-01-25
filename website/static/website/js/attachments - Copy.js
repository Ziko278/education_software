/*---------- uploads ----------*/
// Document ready function to ensure the script runs after the DOM is fully loaded.
$(document).ready(function(){

// =================start iteration ==================
$('#tetsrun').on('click', function() {

for (i = 1; i<6; i++){
  
  var file = $('#item-uploaded'+i)[0].files[0];
  var reader = new FileReader();
  
  reader.onload = function(e) {
    var fileData = e.target.result;
    var fileType = file.type;
    
    var link = $('<a>').attr('href', fileData).attr('download', file.name).text(file.name);
    link.on('click', function(event) {
      if (fileType.startsWith('image/') || fileType.startsWith('application/pdf')) {
        event.preventDefault();
        var embed = $('<embed>').attr('src', fileData).attr('type', fileType).attr('width', '100%').attr('height', '500px');
        $('#attachment1').html(embed);
      } else {
        // Do nothing, let the browser handle the download
      }
    });
    $('#attachment'+i).html(link);
  };
  
  reader.readAsDataURL(file);
  
  
}

  })


  // ================================ end iteration ==========================

  // if($("#item-uploaded1") == ""){
   
  // } else {
  // $("#remove-attachment").show()
  // }




  
  // if($("#item-uploaded1") == ""){
   
  // } else {
  // $("#remove-attachment").show()
  // }

  

  



















  // $("#remove-attachment").click(function(){
  //     $("#item-uploaded1").val("")
  //     $("#remove-attachment").hide()
  //     })

   


  
  //   $('#item-uploaded1').on('change', function() {
  //     if ($("#attachment1") == "No file attached"){
  //       alert("attachment found!")
  //     }

  // });

})