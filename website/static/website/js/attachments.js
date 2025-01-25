/*---------- uploads ----------*/
// Document ready function to ensure the script runs after the DOM is fully loaded.
$(document).ready(function(){

  // =================start iteration ==================
    $(".uploads-item").click(function(){
      


      for (let i = 1; i <= 11; i++) {
        $(`#item-uploaded-${i}`).on('change', function() {
          if($(`#item-uploaded-${i}`).val() ==""){
            $(`#attachment-${i}`).text("No file attached")
          } else {

            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function(e) {
              var fileData = e.target.result;
              $(`#attachment-${i}`).html(`<a href="${fileData}" download="${file.name}">${file.name}</a>`);
            };
            reader.readAsDataURL(file);
          }
          });
        }
        // ================================ end iteration ==========================
    })

  
  })
  
