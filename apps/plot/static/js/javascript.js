$( document ).ready(function() {
    $('#users_interaction').on('click', function(){
        $('#plot_img').attr('src','../media/plot/users_interaction.png');
        $('.panel-heading').text('Interacción entre los participantes');
    });
    $('#users_speak').on('click', function(){
        $('#plot_img').attr('src','../media/plot/users_speak.png');
        $('.panel-heading').text('Tiempo de habla por participante');
    });
});
