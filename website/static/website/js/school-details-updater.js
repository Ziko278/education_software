details = [
  {"fieldset_legend": "Ownership", "group": "ownership",  "btn1": "Private", "btn2": "Mission", "btn3": "Government"},
  {"fieldset_legend": "Faith Based", "group": "faith",  "btn1": "Christian", "btn2": "Islamic", "btn3": "Mixed"},
  {"fieldset_legend": "Bus Service",  "group": "transport", "btn1": "School Owned", "btn2": "3rd Party", "btn3": "Mixed"},
  {"fieldset_legend": "Hostel Accommodation",  "group": "hostel", "btn1": "Boarding Only", "btn2": "Day Only", "btn3": "Mixed"},
  {"fieldset_legend": "Gender", "group": "gender",  "btn1": "Boys Only", "btn2": "Girls Only", "btn3":"Mixed"}

]

placeholders = [
    {"entry": "Name_of_school", "placeholder": "Name of school"},
    {"entry": "Address", "placeholder": "Address line 1"},
    {"entry": "Address2", "placeholder": "Address line 2"},
    {"entry": "Area", "placeholder": "Area"},
    {"entry": "City", "placeholder": "City"},
    {"entry": "LGA", "placeholder": "Local Government Area"},
    {"entry": "state", "placeholder": "State"},
    {"entry": "email", "placeholder": "School Email"},
    {"entry": "phone", "placeholder": "School Telephone number"},
    {"entry": "website", "placeholder": "School Website"}


]
updated_data = {}
updated_data['transaction'] = 'update'
// ------------------------------- function to populate input fields-------------------------------

$(document).ready(function () {
  // Dynamically add radio button groups for each category (details array)
  let detail_corrector = "";
  const count_items = details.length;

  for (let i = 0; i < count_items; i++) {
      detail_corrector += `
          <fieldset name="" class="wrap-reviewer-page" style="width: 100%; display: flex; justify-content: space-between; align-items: center;">
            <legend>${details[i].fieldset_legend}</legend>

            <!-- Container for radio buttons -->
            <div class="reviewer-page" style="display: flex; justify-content: space-evenly; flex-grow: 1;">
              <div style="text-align: center;">
                <label for="${details[i].btn1}"><p>${details[i].btn1}</p></label>
                <input type="radio" class="search-selector" name="${details[i].group}" value="${details[i].btn1}" id="${details[i].btn1}" id-linker="${details[i].btn1}-filter">
              </div>

              <div style="text-align: center;">
                <label for="${details[i].btn2}"><p>${details[i].btn2}</p></label>
                <input type="radio" class="search-selector" name="${details[i].group}" value="${details[i].btn2}" id="${details[i].btn2}" id-linker="${details[i].btn2}-filter">
              </div>

              <div style="text-align: center;">
                <label for="${details[i].btn3}"><p>${details[i].btn3}</p></label>
                <input type="radio" class="search-selector" name="${details[i].group}" value="${details[i].btn3}" id="${details[i].btn3}" id-linker="${details[i].btn3}-filter">
              </div>
            </div>
            <p class="radio-link" style="margin-bottom: 1rem;" id="reset-${i}" name-linker="${details[i].group}" content="${details[i].group}">Clear</p>

            <!-- Reset button aligned to the right -->
            <div style="flex-shrink: 0; text-align: right;">

            </div>

          </fieldset>
      `;
  }
  $("#facility-information").html(detail_corrector);

  // ----------------Dynamically add text input fields (placeholders array)----------------------
  let edit_items = "";
  const all_fields = placeholders.length;

  for (let i = 0; i < all_fields; i++) {
      edit_items += `<div class="attachment-content input-container">
                        <div class="input-wrapper">
                          <input type="text" id="detail-${i}" class="information-input" placeholder="" original-value="">
                          <label for="detail-${i}" class="information-input-label">${placeholders[i].placeholder}</label>
                        </div>
                        <div class="attachment-links">
                          <div class="attachment-link update-edit" id="update-edit${i}" prev="" style="display: none;" next="save-edit${i}" id-modifier="detail-${i}">Edit</div>
                          <div class="attachment-link save-edit" id="save-edit${i}" prev="update-edit${i}" style="display: none;" next="undo-edit${i}" id-modifier="${i}">Done</div>
                          <div class="attachment-link undo-edit" id="undo-edit${i}" prev="" style="display: none;" next="update-edit${i}" id-modifier="${i}">Undo</div>
                        </div>
                      </div>


      `;

  }
  $("#address-information").html(edit_items);
  $("#address-information").show();
  $(".information-0").show();

  // ------------------------Event listener for handling page navigation between sections (Next, Back)------------------
  $(document).on("click", ".update-back", function () {
      const target_class = $(this).attr("link");
      $(".information").hide();
      $("." + target_class).show();
  });

  $(document).on("click", ".update-next", function () {
      const target_class = $(this).attr("link");
      $(".information").hide();
      $("." + target_class).show();
  });

  // Event listener for handling the clearing of radio buttons (Clear option)
  $(document).on("click", ".attachment-link", function () {
      const target_name = $(this).attr("name-linker");

      $("#new-" + target_name).text("");
      // Clear the checked state of the corresponding radio buttons
      $("input[name=" + target_name + "]").prop("checked", false);
  });

  // ----------------------load details of the selected school to the input for correction--------------

$(document).on("click", ".correction-btn", function () {

serial = $("#serial").text()
school_name = $("#school_name").text()
ownership = $("#ownership").val()
nursery = $("#nursery").val()
primary = $("#primary").val()
junior = $("#junior").val()
senior = $("#senior").val()
address = $("#address").text()
area = $("#area").text()
city = $("#city").text()
lga = $("#lga").text()
state = $("#state").text()
email = $("#email").text()
telephone = $("#telephone").text()
website  = $("#website ").text()
faith = $("#faith").val()
hostel = $("#hostel").val()
gender = $("#gender").val()
bus = $("#bus").val()
airconditioning = $("#airconditioning").val()
library = $("#library").val()
sports_arena = $("#sports_arena").val()
science_laboratory = $("#science_laboratory").val()
ict_studio = $("#ict_studio").val()
tuck_shop = $("#tuck_shop").val()
primary_6 = $("#primary_6").val()
sickbay = $("#sickbay").val()



$("#detail-0").val(school_name)
$("#detail-1").val(address)
$("#detail-2").val(address)
$("#detail-3").val(area)
$("#detail-4").val(city)
$("#detail-5").val(lga)
$("#detail-6").val(state)
$("#detail-7").val(email)
$("#detail-8").val(telephone)
$("#detail-9").val(website)


  });






  $("#correct-details").click(function(){
    updated_data['transaction'] = 'update'
    $(".attachment-link").hide();
    $(".update-edit").show();
    $(".introduction").hide();
    $(".information").hide();
    $(".information-0").show();
    $(".information-group").show();
    $(".all-search-group").hide();
    $(".attachment-link").hide();
    $(".update-edit").show();
    $(".information-input").prop("disabled", true);

  });

  $(".update-school").click(function(){
    updated_data['transaction'] = 'new'
    $(".introduction").hide();
    $(".information").hide();
    $(".information-0").show();
    $(".information-group").show();
    $(".all-search-group").hide();
    $(".attachment-link").hide();
    $(".information-input").prop("disabled", false);




  })


$(".return-introduction-btn").click(function(){
    $(".introduction").show();
    $(".information-group").hide();
    $(".all-search-group").show()
    // $(".all-search-group").show()
    $(". add-school").hide()
    $("#found_items").hide()

  })


    // Function to clear form inputs
    function clearForm() {
      $('input[type="text"], input[type="email"], input[type="number"]').val('');
    }

$(".search-selector").click(function() {
   search_category = $(this).attr("id-linker")
    $(this).attr("id-linker")
    $(".category").hide()
    $("."+ search_category).show()
        // stateLoading();
    // clear names here



});


// lllllllllllllllllllllll
// kkkkkkkkkkkkkkkkkkkkkkkkkkkkk

$(document).ready(function () {

  let button_blocker = 0;  // Initialize button_blocker as an integer

  // When the button with class '.loader' is clicked
  $(".loader").click(function (event) {
    // Prevent the default action (form submission or button action)
    event.preventDefault();

    // Initialize a flag to track if the form is valid
    let isValid = true;

    // Clear any previous error messages
    $(".error-message").remove();

    // Validate Name: It should not be empty
    if ($("#name").val().trim() === "") {
      isValid = false;
      $("#name").val(""); // Replace placeholder with error message
      $("#name").attr("placeholder", "Name is required."); // Replace placeholder with error message
      $("#name").addClass("error");  // Add error class to input field
      $("#name").after('<span class="error-asterisk" style="color: red;">*</span>'); // Add red asterisk after the input field
      button_blocker++;  // Increment button_blocker by 1
    }

    // Clear error message on keyup for Name
    $("#name").keyup(function() {
      if ($("#name").val().trim() !== "") {
        $("#name").removeClass("error"); // Remove error class from input field
        $("#name").attr("placeholder", ""); // Reset the placeholder
        $("#name").next('.error-asterisk').remove(); // Remove the red asterisk
        button_blocker--;  // Decrement button_blocker by 1
      }
    });

    // Validate Email: It should be in a valid email format
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test($("#email").val().trim())) {
      isValid = false;
      $("#email").val(""); // Replace placeholder with error message
      $("#email").attr("placeholder", "Please enter a valid email address."); // Replace placeholder with error message
      $("#email").addClass("error");  // Add error class to input field
      $("#email").after('<span class="error-asterisk" style="color: red;">*</span>'); // Add red asterisk after the input field
      button_blocker++;  // Increment button_blocker by 1
    }

    // Clear error message on keyup for Email
    $("#email").keyup(function() {
      if ($("#email").val().trim() !== "") {
        $("#email").removeClass("error"); // Remove error class from input field
        $("#email").attr("placeholder", ""); // Reset the placeholder
        $("#email").next('.error-asterisk').remove(); // Remove the red asterisk
        button_blocker--;  // Decrement button_blocker by 1
      }
    });

    // Validate Designation: It should not be empty
    if ($("#designation").val().trim() === "") {
      isValid = false;
      $("#designation").val(""); // Replace placeholder with error message
      $("#designation").attr("placeholder", "Designation is required."); // Replace placeholder with error message
      $("#designation").addClass("error");  // Add error class to input field
      $("#designation").after('<span class="error-asterisk" style="color: red;">*</span>'); // Add red asterisk after the input field
      button_blocker++;  // Increment button_blocker by 1
    }

    // Clear error message on keyup for Designation
    $("#designation").keyup(function() {
      if ($("#designation").val().trim() !== "") {
        $("#designation").removeClass("error"); // Remove error class from input field
        $("#designation").attr("placeholder", ""); // Reset the placeholder
        $("#designation").next('.error-asterisk').remove(); // Remove the red asterisk
        button_blocker--;  // Decrement button_blocker by 1
      }
    });

    // Validate Phone Number: It should be numeric and 10 digits long
    const phonePattern = /^[0-9]{11}$/;
    if (!phonePattern.test($("#number").val().trim())) {
      isValid = false;
      $("#number").val(""); // Replace placeholder with error message
      $("#number").attr("placeholder", "Please enter a valid 11-digit phone number."); // Replace placeholder with error message
      $("#number").addClass("error");  // Add error class to input field
      $("#number").after('<span class="error-asterisk" style="color: red;">*</span>'); // Add red asterisk after the input field
      button_blocker++;  // Increment button_blocker by 1
    }

    // Clear error message on keyup for Phone Number
    $("#number").keyup(function() {
      if ($("#number").val().trim() !== "") {
        $("#number").removeClass("error"); // Remove error class from input field
        $("#number").attr("placeholder", ""); // Reset the placeholder
        $("#number").next('.error-asterisk').remove(); // Remove the red asterisk
        button_blocker--;  // Decrement button_blocker by 1
      }
    });

    // If the form is valid, proceed with the intended action
    if(button_blocker === 0){
      const target_class = $(this).attr("link");
      $(".information").hide();
      $("." + target_class).show();
    }

    // Reset button_blocker
    button_blocker = 0;
  });
});
$(document).on('click', '.update-edit', function() {
  // Get the index of the element clicked
  let index = $(this).attr("id-modifier");

  // Select the input field by id and change the text inside the input
  let thisInput = $("#" + index); // Access input element by its dynamic id
  let initialValue = thisInput.val()
  thisInput.prop("disabled", false); // Enable the input field for editing
  thisInput.attr("original-value",initialValue); // get the original value


  // Hide the current "Edit" button and show the "Done" button
  $(this).hide(); // Hide the "Edit" button
  $("#" + $(this).attr("next")).show(); // Show the "Done" button

  // Optionally, add logic for placeholder changes or other UI adjustments
});
// =========================================   WIP
$(document).on('click', '.save-edit', function() {

  // Get the index of the element clicked
  let index = $(this).attr("id-modifier");

  // Get the input field to save its value
  let thisInput = $("#detail-" + index);

  // Optionally process the value (e.g., save to a database)
  // console.log("Saved value: " + thisInput.val());

  // Disable the input field after saving
  thisInput.prop("disabled", true);
  let originalText = thisInput.attr("original-value")
  let newText =  thisInput.val()


  // Hide the "Done" button and show the "Undo Edit" button
  $(this).hide();
  if(newText == originalText){
    $("#" + $(this).attr("prev")).show();
  } else {

    $("#" + $(this).attr("next")).show();
  }
});
// ============================= WIP
$(document).on('click', '.undo-edit', function() {
  // Get the index of the element clicked
  let index = $(this).attr("id-modifier");

  // Select the input field by id and revert it
  let thisInput = $("#detail-" + index);

  //  $(this).attr("original-value");
  let originalInput = thisInput.attr("original-value"); // Disable the input field to prevent further editing
  thisInput.val(originalInput); // Disable the input field to prevent further editing
  // thisInput.prop("disabled", true); // Disable the input field to prevent further editing
  originalInput = ""

  // Hide the "Undo Edit" button and show the "Edit" button

  $(this).hide();
  $("#" + $(this).attr("next")).show();
});

$(".transfer-info").click(function(){
  submitDetails();
})





// ========transfer information from the found school to the edit input (end)==========

// $(document).on("click", ".information-input", function(){


//   alert($(this).attr("id"))

// })
// ========extract editors details (start)========
$(".load-editor-detail").click(function(){
  person = $("#name").val()
  email = $("#email").val()
  designation = $("#designation").val()
  number = $("#number").val()

  $("#sent-modifier-name").text(person)
  $("#sent-modifier-email").text(email)
  $("#sent-modifier-designation").text(designation)
  $("#sent-modifier-phone").text(number)

  updated_data["modifier_name"] = person
  updated_data["modifier_email"] = email
  updated_data["modifier_designation"] = designation
  updated_data["modifier_number"] = number

});


// ========extract editors details (end)========

// ========extract school details (start)========
$(document).on("click", ".load-school-details", function(){

  // serial
  school = $("#detail-0").val()
//   // ownership
  address = $("#detail-1").val()
  address1 = $("#detail-2").val()
  area = $("#detail-3").val()
  city = $("#detail-4").val()
  lga = $("#detail-5").val()
  state = $("#detail-6").val()
  email = $("#detail-7").val()
  telephone = $("#detail-8").val()
  website = $("#detail-9").val()

  $("#sent-school_name").text("School Name: " + school)
  $("#sent-address").text(address)
  $("#sent-area").text(area)
  $("#sent-lga").text(lga)
  $("#sent-state").text(state)
  $("#sent-email").text(email)
  $("#sent-telephone").text(telephone)
  $("#sent-website").text(website)


  updated_data["school_name"] = school
  updated_data["address"] = address
  updated_data["address1"] = address1
  updated_data["area"] = area
  updated_data["lga"] = lga
  updated_data["city"] = city
  updated_data["state"] = state
  updated_data["email"] = email
  updated_data["telephone"] = telephone
  updated_data["website"] = website

})


// ========extract school details (end)========
// ======== Gender Selection (start) ========
$(document).on("click", "input[name='gender']", function () {
  const gender = $("input[name='gender']:checked").val();
  $("#sent-gender").text('Gender:' + gender);
  updated_data['gender'] = gender
});
// ======== Gender Selection (end) ========

// ======== Faith Selection (start) ========
$(document).on("click", "input[name='faith']", function () {
  const faith = $("input[name='faith']:checked").val();
  $("#sent-faith").text('Faith:' + faith);
  updated_data['faith'] = faith
});
// ======== Faith Selection (end) ========

// ======== Transport Selection (start) ========
$(document).on("click", "input[name='transport']", function () {
  const transport = $("input[name='transport']:checked").val();
  $("#sent-transport").text('Transport:' + transport);
  updated_data['transport'] = transport
});
// ======== Transport Selection (end) ========

// ======== Hostel Selection (start) ========
$(document).on("click", "input[name='hostel']", function () {
  const hostel = $("input[name='hostel']:checked").val();
  $("#sent-hostel").text('Hostel:' +  hostel);
  updated_data['hostel'] = hostel
});
// ======== Hostel Selection (end) ========

// ======== Sections Selection (start) ========
$(document).on("click", "input[name='section[]']", function () {
  const selectedSections = $("input[name='section[]']:checked").map(function () {
    return $(this).val();
  }).get();

  // Clear previous selections
  $("#selected-values").empty();

  // Append new selected values as list items
  selectedSections.forEach(function (section) {
    $("#selected-values").append($('<li>').text(section));
    updated_data[section] = 'available'
  });
});
// ======== Sections Selection (end) ========

// ======== School Availability Section (start) ========

$(document).on("click", "input[name='search[]']", function () {
  selectedSearchValues = $("input[name='search[]']:checked").map(function () {
    return $(this).val();
  }).get();

  // Clear previous selections
  $("#sent-search").empty();

  // Append new selected search values as list items
  selectedSearchValues.forEach(function (value) {
    $("#sent-search").append($('<li>').text(value +": Available"));
    updated_data[value] = 'available'
  });
});

// ======== School Availability Section (end) ========

$("#clear-all").click(function(){

  clearAll ();
})


});


function clearAll (){
  //.................... clear data in input fields.......................
  $("#name").val("")
  $("#email").val("")
  $("#designation").val("")
  $("#number").val("")


$("#detail-0").val("")
$("#detail-1").val("")
$("#detail-2").val("")
$("#detail-3").val("")
$("#detail-4").val("")
$("#detail-5").val("")
$("#detail-6").val("")
$("#detail-7").val("")
$("#detail-8").val("")
$("#detail-9").val("")

$("input[name='gender']").prop("checked", false)
$("input[name='transport']").prop("checked", false)
$("input[name='hostel']").prop("checked", false)
$("input[name='faith']").prop("checked", false)
$("input[name='ownership']").prop("checked", false)
// $("input[name='search']").prop("checked", false)
// $("input[name='section']").prop("checked", false)
$("input[name='section[]']").prop("checked", false)

$("input[name='search[]']").prop("checked", false)
// $("input[name='search[]']:checked")

// clear all submitted details

$("#sent-modifier-name").text("")
$("#sent-modifier-email").text("")
$("#sent-modifier-designation").text("")
$("#sent-modifier-phone").text("")

$("#sent-school_name").text("")
$("#sent-address").text("")
$("#sent-area").text("")
$("#sent-lga").text("")
$("#sent-state").text("")
$("#sent-email").text("")
$("#sent-telephone").text("")
$("#sent-website").text("")
$("#sent-ownership").text("")
$("#sent-gender").text("")
$("#sent-faith").text("")
$("#sent-transport").text("")
$("#sent-hostel").text("");
$("#selected-values").empty();
$("#sent-search").empty();
}

// Event listener for handling the clearing of radio buttons (Clear option)
$(document).on("click", ".radio-link", function () {
    const target_name = $(this).attr("name-linker");

    $("#new-" + target_name).text("");
    $("#sent-" + target_name).text("");

    // Clear the checked state of the corresponding radio buttons
    $("input[name=" + target_name + "]").prop("checked", false);

});

$(document).on("click", "#submitdetail", function () {
   // Convert object to JSON string
        var jsonString = JSON.stringify(updated_data);
        console.error(jsonString);

        $.ajax({
            url: '/send-update-mail',
            type: 'GET',
            data: { updated_data: jsonString },
            success: function(data) {
                alert(data.message);
                clearAll()
            },
            error: function(xhr, status, error) {
                alert('Error sending data, Try Later');
                console.error('Error sending data:', error);
            }
        });
});