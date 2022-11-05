data = {"vehicles":[
    {"make": "BMW", "models": [
        {
    "model": "X3",
    "years": [{"year": 2003, "fits": true},{"year": 2004, "fits": true},{"year": 2005, "fits": true},{"year": 2006, "fits": true},{"year": 2007, "fits": true},{"year": 2008, "fits": true},{"year": 2009, "fits": true}]
    }
]},
    {"make": "Ford", "models": [
        {
    "model": "Fiesta",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "Focus ST",
    "years": [{"year": "All Years", "fits": ""}]
    },  
        {
    "model": "KA",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "Mustang",
    "years": [{"year": 2015, "fits": true}]
    },
        {
    "model": "Transit",
    "years": [{"year": 2013, "fits": true}]
    }
]},
    {"make": "Jaguar", "models": [
        {
    "model": "F-Type",
    "years": [{"year": "", "fits": true}]
    }
]},
    {"make": "Land Rover", "models": [
        {
    "model": "Defender",
    "years": [{"year": 2019, "fits": true}]
    },
        {
    "model": "Discovery",
    "years": [{"year": 2017, "fits": true}]
    }
]}, 
    {"make": "Mercedes", "models": [
        {
    "model": "A Class",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "B Class",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "C Class",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "E Class",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "S Class",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "Sprinter",
    "years": [{"year": 2019, "fits": true},{"year": 2020, "fits": true},{"year": 2021, "fits": true}]
    }            
]},
    {"make": "Peugeot", "models": [
        {
    "model": "3008",
    "years": [{"year": 2014, "fits": true}]
    }
]},
    {"make": "Porsche", "models": [
        {
    "model": "Boxter",
    "years": [{"year": 2014, "fits": true}]
    }
]},
    {"make": "Range Rover", "models": [
        {
    "model": "Discovery",
    "years": [{"year": 2017, "fits": true}]
    },
        {
    "model": "Evoque",
    "years": [{"year": 2021, "fits": true}]
    },
        {
    "model": "Sport",
    "years": [{"year": 2013, "fits": true}]
    }   
]},
    {"make": "Tesla", "models": [
        {
    "model": "Model 3",
    "years": [{"year": 2018, "fits": true}]
    }
]},  
    {"make": "Vauxhall", "models": [
        {
    "model": "Astra",
    "years": [{"year": "All Years", "fits": ""}]
    },
        {
    "model": "Corsa",
    "years": [{"year": "All Years", "fits": ""}]
    },   
        {
    "model": "Insignia",
    "years": [{"year": "All Years", "fits": ""}]
    }     
]}, 
    {"make": "Volvo", "models": [
        {
    "model": "XC60",
    "years": [{"year": 2017, "fits": true}]
    },
        {
    "model": "XC90",
    "years": [{"year": 2015, "fits": true}]
    } 
]}
]}

make = document.getElementById('make')
model = document.getElementById('model')    
year = document.getElementById('year')

for(i = 0; i < data.vehicles.length; i++){ 
    myOption = document.createElement("option");
    myOption.text = data.vehicles[i].make;
    myOption.value = i
    make.appendChild(myOption)
}
 
function changeMake(sel){
    document.getElementById('fits').innerHTML = "Fill out the query above to check if it will fit your vehicle"
    for (i = model.options.length; i > 0; i--) {
        model.options[i] = null;
    }
    for (i = year.options.length; i > 0; i--) {
        year.options[i] = null;
    }
       
    temp = data.vehicles[sel]
    console.log(temp)
    for(i=0;i<temp.models.length; i++){
        myOption = document.createElement("option");
        myOption.text = temp.models[i].model
        myOption.value = i
        model.appendChild(myOption)
    }
}

function changeModel(sel){
    for (i = year.options.length; i > 0; i--) {
        year.options[i] = null;
    }
       
    temp = data.vehicles[make.value].models[sel]
    console.log("temp", temp)
    
    for(i=0;i<temp.years.length; i++){
        myOption = document.createElement("option");
        myOption.text = temp.years[i].year
        myOption.value = i
        year.appendChild(myOption)
    }
}

function changeYear(sel){
    
    if(data.vehicles[make.value].models[model.value].years[sel].fits === true){
        document.getElementById('fits').innerHTML = "Pedlock does fit this vehicle"
    }else if(data.vehicles[make.value].models[model.value].years[sel].fits === false){
        document.getElementById('fits').innerHTML = "Pedlock does NOT fit this vehicle"
    }else{
        document.getElementById('fits').innerHTML = "We are unsure if Pedlock fits this vehicle"
    }
}