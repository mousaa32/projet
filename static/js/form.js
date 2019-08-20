// $(document).ready(function() {
//     $('form').on('submit',function(event){
//        $.ajax({
//             data :{
//             matricule:$('#matricule').val(),
//             prenom:$('#prenom').val(),
//             nom:$('#nom').val(),
//             email:$('#email').val(), 
//             dateNaissance:$('#dateNaissance').val()
//             },
//             type :'POST',
//             url :'/insert',
//             alert(result)
//         })
//         .done(function(data){
//             $('#matricule').val(' ');
//             $('#prenom').val(' ');
//             $('#nom').val(' ');
//             $('#email').val(' ');
//             $('#dateNaissance').val(' ')
//         });
//             if (data.error){
//                 $('#errorAlert').text(data.error).show();
//                 $('#successAlert').hide();
//             }
//             else{
//                 $('#successAlert').text(data.nom).show();
//                 $('#errorAlert').hide();
//             }
//         });
//             event.preventDefault();
//     });


    $(function() {

        // test to ensure jQuery is working
        console.log("whee!")
    
        // disable refresh button
        $("#refresh-btn").prop("disabled", true)
    
    
        $("#filiere_select").change(function() {
    
            // grab value
            var filiere_id = $("#filiere_select").val();
    
            // send value via GET to URL /<department_id>
            var get_request = $.ajax({
                type: 'GET',
                url: '/filiere/' + filiere_id + '/',
            });
    
            // handle response
            get_request.done(function(data) {
    
                // data
                console.log(data)
    
                // add values to list 
                var option_list = [
                    ["", "Select an classe"]
                ].concat(data);
                $("#classe_select").empty();
                for (var i = 0; i < option_list.length; i++) {
                    $("#classe_select").append(
                        $("<option></option>").attr("value", option_list[i][0]).text(option_list[i][1]));
                    $("#frais_ins").append(
                        $("<input/>").attr("value", [i][2])
                    );
                }
                // show model list
                $("#classe_select").show();
            });
        });
    });
 




    $( document ).ready(function() {
        $('#Filière').change(function(){ 
           var x = document.getElementById("Filière").value;
           $('#classe').children('option:not(:first)').remove();
           $('#mont_ins').val("");
           $('#mensualite').val("");
           $('#total_ins').val("");
            $.ajax({ 
              type: "GET",
              url: "http://127.0.0.1:5000/"+x,
           });
        });
     });
      
     $( document ).ready(function() {
        $('#Filière').change(function(){ 
           var x = document.getElementById("Filière").value;
           $.ajax({ 
              type: "GET",
              contentType: 'application/json; charset=utf-8',
              url: "http://127.0.0.1:5000/filiere&"+x,
              success: function(liste_classe){
                 $.each(liste_classe,function(index,d){
                    $("#classe").append("<option value="+ d.id +">" + d.libelle + "</option>");
                 });
              }
           });
        });
     });
      
     /****************************************ACTION NOUVEAU LISTE DES FILIERES A AFFICHER****************/
      
      
      
      /********************************AJAX CLASSE****************************/
     $( document ).ready(function() {
        $('#classe').change(function(){ 
           var x = document.getElementById("classe").value;
           $('#mont_ins').val("");
           $('#mensualite').val("");
           $('#total_ins').val("");
     /*                document.getElementById("response").innerHTML = "You selected: " + x;
     */    $.ajax({ 
              type: "GET",
              url: "http://127.0.0.1:5000/classe&"+x,
           });
        });
     });
      
     $( document ).ready(function() {
        $('#classe').change(function(){ 
           var x = document.getElementById("classe").value;
           $.ajax({ 
              type: "GET",
              contentType: 'application/json; charset=utf-8',
              url: "http://127.0.0.1:5000/classe&"+x,
              success: function(liste_ele_classe){
                 $.each(liste_ele_classe,function(index,d){
                    $('#mont_ins').val(d.mont_ins);
                    $('#mensualite').val(d.mensualite);
                    $('#total_ins').val(d.mont_ins+d.mensualite);    
                 });
              }
           });
        });
     });
     /*********************************************ACTION BOUTON RADIO****************************/
     $(function() {
        var matricule = document.getElementById("matricule").value;
        $('#Ancien').on('click',function(){
        //    document.getElementById("text-radio").innerHTML = "REINSCRIPTION";
           document.getElementById('enregistrer').disabled = true;
      
           $('#Filière').children('option:not(:first)').remove();
           $('#matricule').attr('readonly', false); 
           $('#matricule').val(""); 
           vider();
           lire(); 
           changeColor();
        }); 
        $('#nouveau').on('click',function(){
           document.getElementById("text-radio").innerHTML = "INSCRIPTION";
           changeColor();
           document.getElementById('enregistrer').disabled = false;
      
           $('#matricule').attr('readonly', true);
           $('#matricule').val(matricule);
          /* window.location.reload();*/
           vider();
           ecrire();
      
           $( document ).ready(function() {
               
              $('#Filière').children('option:not(:first)').remove();
              $('#classe').children('option:not(:first)').remove();
         
              /*document.getElementById("response").innerHTML = "You selected: " + x;*/
              $.ajax({ 
                 type: "GET",
                 url: "http://127.0.0.1:5000/listfiliere",
              });
           });
         
        $( document ).ready(function() {
              var x = document.getElementById("fil").value;
              $.ajax({ 
                 type: "GET",
                 contentType: 'application/json; charset=utf-8',
                 url: "http://127.0.0.1:5000/listfiliere",
                 success: function(liste_filiere){
                    $.each(liste_filiere,function(index,d){
      
                       $("#Filière").append("<option value="+ d.id +">" + d.libelle + "</option>");
                    });
                 }
              });
           });
                
        });        
     });
      
     /*******************************************SEARCH APPRENANT******************** */
      
     function ecouteInput(event) {
        var x = window.event.which || window.event.keyCode;
      
        if(x==13){
           var searchmat = document.getElementById("mat").value;
           $.ajax({ 
              type: "GET",
              url: "http://127.0.0.1:5000/search&"+searchmat,
           });
           $.ajax({ 
              type: "GET",
              contentType: 'application/json; charset=utf-8',
              url: "http://127.0.0.1:5000/search&"+searchmat,
      
              success: function(apprenant_find){   
                 $.each(apprenant_find, function(index,d){
                    if(d.prenom){
                       /*document.getElementById("response").innerHTML = "You selected is pliein";*/
      
                       $('#prenom').val(d.prenom);
      
                       $('#nom').val(d.nom);
                       $('#sexe').val(d.sexe);
                        
                       $('#date_naissance').val(convert(d.date_naiss));
                       $('#lieu_naissance').val(d.lieu_naiss);
                       $('#adresse').val(d.adresse);
                       $('#email').val(d.email);
                       $('#telephone').val(d.tel); 
                       $("#Filière").append("<option value="+ d.id_fil +">" + d.nom_fil + "</option>");
                        
                       changeColorText();
                       $('#mat').attr('readonly', true);
                       lire();
                       document.getElementById('boutonenvoi').disabled = false;
      
                       document.getElementById('boutsearch').style.display = 'block';
      
                    }
                    else{
                       document.getElementById('boutonenvoi').disabled = true;
      
                       $.uiAlert({
                          textHead: d.vide,
                          text: '', // Text
                          bgcolor: '#DB2828', // background-color
                          textcolor: '#fff', // color
                          position: 'top-center',// position . top And bottom ||  left / center / right
                          time: 5, // time
                       })                  
                    }
                 });
              },
           });
        }
     }
      
     $('#boutsearch').on('click',function(){
        document.getElementById('boutsearch').style.display = 'none';
        $('#mat').attr('readonly', false);
        $('#mat').val("");
        $('#Filière²').children('option:not(:first)').remove();
        $('#classe').children('option:not(:first)').remove();
      
        vider();
      
     });
      
     /*************************************************CONTROLE CHAMP*****************************/
     newFunction();
     function newFunction() {
        $('.ui.form')
        .form({
           fields: {
              prenom: 'empty',
              nom: 'empty',
              sexe: 'empty',
              date_naissance: 'empty',
              lieu_naissance: 'empty',
              adresse: 'empty',
              email: 'empty',
              telephone: 'empty',
              promo: 'empty',
              fil : 'empty',
              classe : 'empty',
           }
        });
     }
     /*********************************************LES FONCTIONS***********************/
     function convert(str) {
        var date = new Date(str),
           mnth = ("0" + (date.getMonth() + 1)).slice(-2),
           day = ("0" + date.getDate()).slice(-2);
        return [date.getFullYear(), mnth, day].join("-");
     }
     function lire(){
        $('#prenom').attr('readonly', true);
        $('#nom').attr('readonly', true);
        document.getElementById('sexe').disabled=true
        $('#date_naissance').attr('readonly', true);
        $('#lieu_naissance').attr('readonly', true);
        $('#adresse').attr('readonly', true);
        $('#email').attr('readonly', true);
        $('#telephone').attr('readonly', true);
     }
     function ecrire(){
        $('#prenom').attr('readonly', false);
        $('#nom').attr('readonly', false);
        document.getElementById('sexe').disabled=false
        $('#date_naissance').attr('readonly', false);
        $('#lieu_naissance').attr('readonly', false);
        $('#adresse').attr('readonly', false);
        $('#telephone').attr('readonly', false);
        $('#email').attr('readonly', false);
      
        document.getElementById('boutsearch').style.display = 'none';
     }
     function vider(){
           $('#prenom').val("");
           $('#nom').val("");
           $('#sexe').val("");
           $('#date_naissance').val("");
           $('#lieu_naissance').val("");
           $('#adresse').val("");
           $('#email').val("");
           $('#telephone').val("");        
           $('#fil').val("");
           $('#classe').val("");
           $('#mont_ins').val("");
           $('#mensualite').val("");
           $('#total_ins').val(""); 
     }
      
     function changeColor(){
      
        var x = document.getElementsByClassName("champ");
        var y = document.getElementsByClassName("lab");
        for (var i=0 ; i < x.length ; i++) {
           x[i].style.borderColor = "#dfe0e0";
           x[i].style.backgroundColor = "white";
        }
        for (var j=0 ; j < y.length ; j++) {      
           y[j].style.color="black";
        }
     }
      
     function changeColorText(){
      
        var x = document.getElementsByClassName("champ");
        for (var i=0 ; i < x.length ; i++) {
           x[i].style.color = "black";
        }
      
      
     }