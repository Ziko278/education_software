// import {schools} from "./schools.js"
// import { schools } from './schools.js';

$(document).ready(function(){
    // Schools data
 
        
    
    // Handle keyup event for the search input
    $("#school-name-search").keyup(function(){
        let entered_letters = $(this).val().toLowerCase();  // Convert to lowercase for case-insensitive search
        let returned_list = "";
        
        // Filter schools by school_name
        let filtered_list = schools.filter(function(obj) {
            return obj.school_name.toLowerCase().includes(entered_letters); // Case insensitive match
        });

        // If there are filtered schools, generate HTML for the results
        if (filtered_list.length > 0) {
            filtered_list.forEach(function(single_item) {
                returned_list += `<li class="selection" 
                                    serial="${single_item.serial}" 
                                    ownership="${single_item.ownership}" 
                                    nursery="${single_item.nursery}" 
                                    primary="${single_item.primary}" 
                                    junior="${single_item.junior}" 
                                    senior="${single_item.senior}" 
                                    address="${single_item.address}" 
                                    area="${single_item.area}" 
                                    city="${single_item.city}" 
                                    lga="${single_item.lga}" 
                                    state="${single_item.state}" 
                                    email="${single_item.email}" 
                                    telephone="${single_item.telephone}" 
                                    website="${single_item.website}" 
                                    faith="${single_item.faith}" 
                                    hostel="${single_item.hostel}" 
                                    gender="${single_item.gender}" 
                                    bus="${single_item.bus}" 
                                    airconditioning="${single_item.airconditioning}" 
                                    library="${single_item.library}" 
                                    sports_arena="${single_item.sports_arena}" 
                                    science_laboratory="${single_item.science_laboratory}" 
                                    ict_studio="${single_item.ict_studio}" 
                                    tuck_shop="${single_item.tuck_shop}" 
                                    primary_6="${single_item.primary_6}" 
                                    sickbay="${single_item.sickbay}">
                                    ${single_item.school_name}</li>`;
            });
            $("#found_items").html(returned_list).show(); // Display the results
            $(".business-search-result").text(""); // Reset the business search result text
            $("#correct-details").hide(); // Hide the correct details section
            $(".all-search-group").show(); // Show the search results section
            $(".add-school").hide(); // Hide the "Add School" section if results are found
        } else {
            // If no matches are found, show the "Add School" section
            $(".all-search-group").hide(); // Hide search results section
            $(".add-school").show(); // Show the "Add School" section
        }
    });

    
    // Handle "New Search" button click
    // $(document).on("click",".new-search", function(){

    // // } )
    $(".new-search").click(function() {
        $(".all-search-group").show(); // Show search results section
        $(".add-school").hide(); // Hide "Add School" section
        $("#school-name-search").val(""); // Clear search input
        $("#found_items").html(""); // Clear search results
        $(".introduction").show();
        $(".information-group").hide();      
        $(".all-search-group").show();
        $(".business-search-result").hide(); // hide the business result section
        $("#correct-details").hide(); // hide the correction button
        
       
        // clearEntries();
        $("#name").text("cleared");
        $("#email").text("");
        $("#designation").text("");
        $("#number").text("");
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
        
        
      
        $("#checkbox1").val("");
        $("#checkbox2").val("");
        $("#checkbox3").val("");
        $("#checkbox4").val("");
        $("#checkbox5").val("");
        $("#checkbox6").val("");
        $("#checkbox7").val("");
        $("#checkbox8").val("");
        $("#checkbox9").val("");
    
        // end clearEntries
 



    
    });

    // Handle click event on selection item
    $(document).on("click", ".selection", function() {
        // Collect all attributes of the clicked school
        let school_name = $(this).text();
        let serial = $(this).attr("serial");
        let ownership = $(this).attr("ownership");
        let nursery = $(this).attr("nursery");
        let primary = $(this).attr("primary");
        let junior = $(this).attr("junior");
        let senior = $(this).attr("senior");
        let address = $(this).attr("address");
        let area = $(this).attr("area");
        let city = $(this).attr("city");
        let lga = $(this).attr("lga");
        let state = $(this).attr("state");
        let email = $(this).attr("email");
        let telephone = $(this).attr("telephone");
        let website = $(this).attr("website");
        let faith = $(this).attr("faith");
        let hostel = $(this).attr("hostel");
        let gender = $(this).attr("gender");
        let bus = $(this).attr("bus");
        let airconditioning = $(this).attr("airconditioning");
        let library = $(this).attr("library");
        let sports_arena = $(this).attr("sports_arena");
        let science_laboratory = $(this).attr("science_laboratory");
        let ict_studio = $(this).attr("ict_studio");
        let tuck_shop = $(this).attr("tuck_shop");
        let primary_6 = $(this).attr("primary_6");
        let sickbay = $(this).attr("sickbay");


$("#serial").text(serial)
$("#school_name").text(school_name)
$("#ownership").val(ownership)
$("#nursery").val(nursery)
$("#primary").val(primary)
$("#junior").val(junior)
$("#senior").val(senior)
$("#address").text(address)
$("#area").text(area)
$("#city").text(city)
$("#lga").text(lga)
$("#state").text(state)
$("#email").text(email)
$("#telephone").text(telephone)
$("#website ").text(website)
$("#faith").val(faith)
$("#hostel").val(hostel)
$("#gender").val(gender)
$("#bus").val(bus)
$("#airconditioning").val(airconditioning)
$("#library").val(library)
$("#sports_arena").val(sports_arena)
$("#science_laboratory").val(science_laboratory)
$("#ict_studio").val(ict_studio)
$("#tuck_shop").val(tuck_shop)
$("#primary_6").val(primary_6)
$("#sickbay").val(sickbay)

        // Display school details in business result
        // $("#nature_of_business").text("School Location: " + ownership);
        $("#school-name-search").val(""); // Clear search input
        $("#found_items").hide(); // Hide search results
        $(".business-search-result").show(); // Show the business result section
        $("#correct-details").show(); // Show school details


    });



   
       $(".corrector").click(function(){
        namer = $("#School_name").text()
        $("#detail-1").val(namer)
        $("#detail-1").prop("disabled", true)
        $(this).prop("disabled", true)    



       })

       $(".update-edit").click(function(){
        // namer = $("#School_name").hide()
        // $("#detail-1").hide()
        $("#detail-1").prop("disabled", false)
        $(".save-edit").show()
        // $(".editor-content").show()
        $(".editor-input").show()
        $(this).hide()
       })
  
       $(".undo-edit").click(function(){
        $("#detail-1").show()
        $(".editor-input").hide()
        $(".save-edit").show()
        $(this).hide()
       })
       $(".save-edit").click(function(){
        $(".update-edit").show()
        $("#detail-1").prop("disabled", true)

        $(this).hide()
       })

});

// $(function clearEntries(){



  
// })