/*---------- iterations ----------*/
// Document ready function to ensure the script runs after the DOM is fully loaded.
$(document).ready(function(){


file_loader=[
        {'id':'first-upload', 'description': 'Passport Data Page'},
        {'id':'second-upload', 'description': 'Passport Last Page'},
        {'id':'third-upload', 'description': 'Diploma/Bachelors/Masters Mark Sheet & Degree Certificate'},
        {'id':'fourth-upload', 'description': 'Statement of Purpose'},
        {'id':'fifth-upload', 'description': 'TOEFL / IELTS Score Card'},
        {'id':'sixth-upload', 'description': '10th & 12th Scorecard'},
        {'id':'seventh-upload', 'description': 'Resume'},
        {'id':'eighth-upload', 'description': 'Letter of Recommendations'},
        {'id':'nineth-upload', 'description': 'Work Experience documents (if any)'}
    ]

  //   review_page = `<div class="uploads-content" style="display: none;">
  //   <div class="uploads-top">
  //     <div class="uploads-back">Review documents</div>
  //     <!-- <div class="uploads-next" id="item1"></div> -->
  //   </div>

  //       <div class="">
  //         <div class="applicant-data"><div>Name: </div><p id="submitted-name"></p></div>
  //         <div class="applicant-data"><div>Telephone: </div><p id="submitted-phone"></p></div>
  //         <div class="applicant-data"><div>Email: </div><p id="submitted-email"></p></div>
  //         <div class="applicant-data"><div>Proposed date: </div><p id="submitted-date"></p></div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x" id="icon1"></i></p>
  //         <div id="attachment1">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div class="attachment-content">
  //         <div id="attachment2">No file attached</div>
  //         <!-- <div class="confirm-attached"><i class="fas fa-check"></i></div> -->

  //         </div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment3">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment4">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment5">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment6">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment7">No file attached</div>
  //       </div>
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-x"></i></p>
  //         <div id="attachment8">No file attached</div>
  //       </div>                  
  //       <div class="reviewer-page">
  //         <p><i class="fas fa-minus optional"></i></p>
  //         <div id="attachment9">optional</div>
  //       </div>

      
  //   <div class="uploads-navigation">
  //     <button type="submit" class="uploads-back uploads-btn">back</button>
  //     <!-- <a href="../../../../../../../Desktop/To send an attachment from an input form with the id freel.html">use this to create a review page</a> -->
  //     <button class="uploads-next uploads-btn">next</button>
  //   </div>
  //   </div>
  // </div>
  // `

// $('#tetral').click(function(){
    runs = file_loader.length
    line = ''
    for (i = 0; i < runs; i++ ){

       line += `<div class="uploads-content" id="${file_loader[i].id}" style="display: none;">
    <div class="uploads-top">
      <div class="">${file_loader[i].description}</div>
      <div class="">Item ${i +1} of 9</div>
    </div>
    <div class="uploads-item">
      <input type="file" class="uploaded=items" tempt_id="remove-attachment${i +1}"></input>
      <div class="mool" temp_id ="remove-attachment${i +1}">
        <div id="remove-attachment${i +1}" style="display: block;">Remove</div>
      </div>
    </div>
    <div class="uploads-navigation">
      <button type="submit" class="uploads-back uploads-btn">back</button>
      <button class="uploads-next uploads-btn">next</button>
    </div>

  </div>`        
      


    }

    $('#generated-upload-form').html(line)
    $('#first-upload').show()
    // $('#review-holder').html(review_page)

// })



  
  
  })