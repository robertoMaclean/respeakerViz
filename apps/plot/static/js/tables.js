var interaction_table = '<table class="table" id="interaction_table">'
interaction_table += '<thead>'
interaction_table += '<tr>'
interaction_table += '<th class="table-head">Emisor/Receptor</th>'  
for(var i=1;i<5;i++){
    interaction_table += '<th class="table-head">Usuario '+i+'</th>'      
}
interaction_table += '</tr>'
interaction_table += '</thead>'
interaction_table += '<tbody>'

for(var i=0;i<data.usersInteraction.length;i=i+3){     
    interaction_table += '<tr>'    
    interaction_table += '<th class="table-head">Usuario '+data.usersInteraction[i]['emisor']+'</th>'
    console.log(data.usersInteraction[i]['emisor'],data.usersInteraction[i]['receptor'] )
    if(data.usersInteraction[i]['emisor'] == 1){
        interaction_table += '<td>0</td>'
        interaction_table += '<td>'+data.usersInteraction[i]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+1]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+2]['value']+'</td>'
    }else if(data.usersInteraction[i]['emisor'] == 2){
        interaction_table += '<td>'+data.usersInteraction[i]['value']+'</td>'
        interaction_table += '<td>0</td>'
        interaction_table += '<td>'+data.usersInteraction[i+1]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+2]['value']+'</td>'
    }else if(data.usersInteraction[i]['emisor'] == 3){
        interaction_table += '<td>'+data.usersInteraction[i]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+1]['value']+'</td>'
        interaction_table += '<td>0</td>'
        interaction_table += '<td>'+data.usersInteraction[i+2]['value']+'</td>'
    }else{
        interaction_table += '<td>'+data.usersInteraction[i]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+1]['value']+'</td>'
        interaction_table += '<td>'+data.usersInteraction[i+2]['value']+'</td>'
        interaction_table += '<td>0</td>'
    }
    
    interaction_table += '</tr>'            
}
interaction_table += '</tbody>'
interaction_table += '</table>'

interv = '<th class="table-head">Intervenciones</th>'
interv += '<td>'+data.usersIntDur[0].length+'</td>'
interv += '<td>'+data.usersIntDur[1].length+'</td>'
interv += '<td>'+data.usersIntDur[2].length+'</td>'
interv += '<td>'+data.usersIntDur[3].length+'</td>'

interv_time = '<th class="table-head">Duración Intervenciones</th>'
interv_time += '<td>'+get_sum(data.usersIntDur[0])+'</td>'
interv_time += '<td>'+get_sum(data.usersIntDur[1])+'</td>'
interv_time += '<td>'+get_sum(data.usersIntDur[2])+'</td>'
interv_time += '<td>'+get_sum(data.usersIntDur[3])+'</td>'

speak_time = '<th class="table-head">Duración habla</th>'
speak_time += '<td>'+data.usersTime[0]['y']+'</td>'
speak_time += '<td>'+data.usersTime[1]['y']+'</td>'
speak_time += '<td>'+data.usersTime[2]['y']+'</td>'
speak_time += '<td>'+data.usersTime[3]['y']+'</td>'

vol_prom = '<th class="table-head">Intensidad promedio</th>'
vol_prom += '<td>'+data.usersVolAVG[0]['y']+'</td>'
vol_prom += '<td>'+data.usersVolAVG[1]['y']+'</td>'
vol_prom += '<td>'+data.usersVolAVG[2]['y']+'</td>'
vol_prom += '<td>'+data.usersVolAVG[3]['y']+'</td>'

var table_up = '<table class="table" id="intervention_table">'
table_up += '<thead>'
table_up += '<tr>'
table_up += '<th class="table-head"></th>'  
for(var i=1;i<5;i++){
    table_up += '<th class="table-head">Usuario '+i+'</th>'      
}
table_up += '</tr>'
table_up += '</thead>'
table_up += '<tbody>'
table_up += '<tr>'

var table_down = '</tr>' 
table_down += '</tbody>'
table_down += '</table>'

interv_table = table_up
interv_table += interv
interv_table += '</tr>'  
interv_table += '<tr>'
interv_table += interv_time
interv_table += table_down 

summary_table = table_up
summary_table += interv
summary_table += '</tr>'  
summary_table += '<tr>'
summary_table += interv_time
summary_table += '</tr>'
summary_table += '<tr>'
summary_table += speak_time
summary_table += '</tr>'
summary_table += '<tr>'
summary_table += vol_prom
summary_table += table_down 


summary_total_table = '<table class="table" id="intervention_table">'
summary_total_table += '<thead>'
summary_total_table += '<tr>'
summary_total_table += '<th class="table-head"></th>'  
summary_total_table += '</tr>'  
summary_total_table += '</thead>'
summary_total_table += '<tbody>'
summary_total_table += '<tr>' 
summary_total_table += speak_time
summary_total_table += '</tr>' 
summary_total_table += '</tbody>'

