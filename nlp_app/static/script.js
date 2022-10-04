function uploadFile(form)
{
    const formData = new FormData(form);
    var oOutput = document.getElementById("static_file_response")
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "upload_static_file", true);
    oReq.onload = function(oEvent) {
        if (oReq.status == 200) {
            console.log(oReq.response)
            var response = JSON.parse(oReq.response)
            show_data(response.filename);
        }
    };
    let flag = document.querySelector('.section-img')
    if (flag !== null) document.querySelector('.section-img').style.display = 'none';
    console.log("Sending file!")
    oReq.send(formData);
};
 

function show_data(name){
    document.querySelector('.main-display').style.overflow = 'scroll';
    console.log(name)
    $.ajax({
        data:{
            filename:name
        },
        type: 'POST',
        url: '/showdata',
    })
    .done(function (data) {
        $('#display-data').html(data.df);
    });
};


document.getElementById('drop-null').addEventListener('click', function () {
    let preprocess = this.id;
    $.ajax({
        data: {
            'preprocess': preprocess
        },
        type: 'POST',
        url: '/preprocessing'
    })
    .done(function (data) {
        df = data.df
         document.getElementById('display-data').innerHTML = df
    });

});


document.getElementById('drop-column').addEventListener('click', function () {
    let preprocess = this.id;

    document.getElementById('dropcolumn-form').style.display = 'flex';
    document.getElementById('dropcolumn-btn').addEventListener('click', function(e) {
        let columnName = document.getElementById('column-name').value;

        $.ajax({
            data: {
                'preprocess': preprocess,
                'columnName': columnName
            },
            type: 'POST',
            url: '/preprocessing'
        })
        .done(function (data) {
            df = data.df
             document.getElementById('display-data').innerHTML = df
        });
    });
    

});



document.getElementById('encode-columns').addEventListener('click', function(e) {
    let preprocess = this.id;
    let column = '';

    document.getElementById('encode-form').style.display = 'flex';

    document.getElementById('encode-btn').addEventListener('click', function (e) {
        column = document.getElementById('column').value;
        let categoryValue = document.getElementById("column-category-select");
        category = categoryValue.options[categoryValue.selectedIndex].value;
        $.ajax({
            data: {
                'category': category,
                'preprocess': preprocess,
                'column': column
            },
            type: 'POST',
            url: '/preprocessing'
        })
        .done(function (data) {
            df = data.df;
            document.getElementById('display-data').innerHTML = df;
        });
        e.preventDefault();
    });

});



document.getElementById('replace-values').addEventListener('click', function() {
    let preprocess = this.id;
    document.getElementById('replace-form').style.display = 'flex';

    document.getElementById('replace-with-value').addEventListener('change', function() {
        if (this.value === 'other-value') document.querySelector('.replace-num-value').style.display = 'flex';

        if (this.value !== 'other-value') document.querySelector('.replace-num-value').style.display = 'none';

    });

    document.getElementById('replace-btn').addEventListener('click', function(e) {
        let replaceValueColumnName = document.getElementById("replace-null-value-column").value
        let replace = document.getElementById("replace-with-value");
        let replaceWithValue = replace.options[replace.selectedIndex].value;
        let numValue;

        if (replaceWithValue === 'other-value') numValue = document.getElementById('replace-num-value').value;

        $.ajax({
            data: {
                'preprocess' : preprocess,
                'replaceValueColumnName' : replaceValueColumnName,
                'replaceWithValue' : replaceWithValue,
                'numValue' : numValue
            },
            type: 'POST',
            url: '/preprocessing'
        })
        .done(function (data) {
            df = data.df;
            document.getElementById('display-data').innerHTML = df;
        });
        e.preventDefault();
    });
    
})

$('#data-info li').click(function () {
    info = this.id;
    document.getElementById('display-data').style.display ='block';
    document.getElementById('display-code').style.display ='none';
    $.ajax({
        data: {
            'info': info,
        },
        type: 'POST',
        url: '/datainfo',
    })
    .done(function (data) {
        let flag = document.querySelector('.section-img')
        if (flag !== null) document.querySelector('.section-img').style.display = 'none';
        document.getElementById('display-data').innerHTML = data.info;
    });
});


$('#showdata').click(function() {
    let data =this.id;
    document.querySelector('.main-display').style.overflow = 'scroll';
    $.ajax({
        data: {
            'data' : data
        },
        type: 'POST',
        url: '/printdata'
    })
    .done(function (data) {
        df = data.df;
        let flag = document.querySelector('.section-img')
        if (flag !== null) document.querySelector('.section-img').style.display = 'none';
        document.getElementById('display-code').style.display ='none';
        document.getElementById('display-data').style.display ='block';
        document.getElementById('display-data').innerHTML = df;
    });
});


$('#get-code').click(function() {
    let data = this.id
    console.log('clicked');
    document.getElementById('display-code').style.display ='block';

     $.ajax({
        data: {
            'data' : data
        },
        type: 'POST',
        url: '/printcode'
    })
    .done(function (data) {
        let flag = document.querySelector('.section-img')
        if (flag !== null) document.querySelector('.section-img').style.display = 'none';
        document.getElementById('display-data').style.display ='none';
        document.getElementById('display-code').innerHTML = data.code;
    });
});


modal = document.querySelectorAll('.modal');
btnCloseModal = document.querySelectorAll('.close-modal');
btnSubmit = document.querySelectorAll('.form-btn');
for( let i=0; i<modal.length; i++)
{
    btnCloseModal[i].addEventListener('click', function() {
        modal[i].style.display = 'none';
    });
}
for( let i=0; i<btnSubmit.length; i++)
{
    btnSubmit[i].addEventListener('click', function() {
        modal[i].style.display = 'none';
    });
}

$('#cluster li').click(function(e) {
    selected_model = this.id;
    console.log('clicked');
    document.getElementById('cluster-form').style.display = 'flex';
    document.getElementById('cluster-btn').addEventListener('click', function(e) {
        cluster_size = document.getElementById('cluster-size').value;
        sim_thresh = document.getElementById('sim-thresh').value;
        console.log("cluster size", cluster_size)
        console.log("sim_thresh", sim_thresh)

        $.ajax({
            data: {
                'sim_thresh': sim_thresh,
                'cluster_size': cluster_size,
            },
            type: 'POST',
            url: '/clustering'
        })
        .done(function (data) {
            clusters = data.clusters
            document.getElementById('clustrs').innerHTML = clusters
        });
    })
})


$('#train li').click(function (e) {
    selected_model = this.id;
    document.getElementById('train-form').style.display = 'flex';

    document.getElementById('train-btn').addEventListener('click', function (e) {

        let output = "";
          var markedCheckbox = document.getElementsByName('output');
          for (var checkbox of markedCheckbox) {
            if (checkbox.checked)
              output = checkbox.value
          }
        let input = ""

        var markedCheckbox = document.getElementsByName('input');  
        for (var checkbox of markedCheckbox) {  
          if (checkbox.checked) {

              input += checkbox.value + ", ";
          }
        }
        console.log("output", output)
        console.log("input", input)
        console.log(input.substring(0, input.length-2))
        input = input.substring(0, input.length-2)
        test_size = document.getElementById('test-size').value;

        $.ajax({
            data: {
                'output': output,
                'input': input,
                'selected_model': selected_model,
                'test_size': test_size,
            },
            type: 'POST',
            url: '/train'
        })
        .done(function (data) {
            metric = data.metric
            document.getElementById('display-error').innerHTML = metric
        });
        e.preventDefault();
    })
});


var Inputexpanded = false;

    function showCheckboxes() {
        var checkboxes = document.getElementById("checkboxes");
        $.ajax({
            type: 'POST',
            url: '/columns'
        })
        .done(function (data) {
            var columns = data.columns
            for ( i of columns)
            {
                checkboxes.innerHTML += `<label class="checkbox-element"><input name="input" type="checkbox" value="${i}" />${i}</label>` 
            }
            if (!Inputexpanded) {
                checkboxes.style.display = "block";
                Inputexpanded = true;
            } else {
                checkboxes.innerHTML = ``;
                checkboxes.style.display = "none";
                Inputexpanded = false;
            }
        });
    }


var Outputexpanded = false;
function showRadioboxes(){
    var radiobuttons = document.getElementById("radiobuttons");
    $.ajax({
        type: 'POST',
        url: '/columns'
    })

    .done(function (data) {
        var columns = data.columns
        console.log("o=Im", columns)
        for ( i of columns)
        {
            radiobuttons.innerHTML += `<label class="checkbox-element"><input type="checkbox" name="output" onclick="onlyOne(this)" value="${i}" />${i}</label>` 
        }
        if (!Outputexpanded ) {
            radiobuttons.style.display = "block";
            Outputexpanded  = true;
        } else {
            radiobuttons.innerHTML = ``;
            radiobuttons.style.display = "none";
            Outputexpanded  = false;
        }
    });
}
function onlyOne(checkbox) {
    var outputboxes = document.getElementsByName('output')
    outputboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}