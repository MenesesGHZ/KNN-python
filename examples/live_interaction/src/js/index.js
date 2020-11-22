window.addEventListener("load",()=>{
	const dataset_input = document.getElementById("dataset-input"),
		dataset_table = $("#dataset"),
		scan_dataset = document.getElementById("scan-dataset"),
		knn_board = document.getElementById("knn-board"),
		knn_graph = document.getElementById("knn-graph"),
		knn_classes = document.getElementById("knn-classes"),
		label = document.getElementById("label");

	// read uploaded dataset	
	scan_dataset.addEventListener("click",()=>{
		const file = dataset_input.files[0];
		Papa.parse(file, {
			complete: function(results) {
				update(results.data);
			}
		});
	});

	const update = (csv_data) =>{
		update_knn_classes(csv_data[0]);
		update_dataset_table(csv_data);
	}
	
	//update inputs
	const update_knn_classes = (variables) =>{
		label_html = `<select id="label" name="label">`;
		knn_classes_html = ``;
		for(let i=0;i<variables.length;i++){
			label_html += `<option value="${variables[i]}">${variables[i]}</option>`;
			knn_classes_html += `
				<div class="row">
				<input type="checkbox" id="${variables[i]}" name="${variables[i]}" value="${variables}">
				<label class="ml-3" for="${variables[i]}">${variables[i]}</label>
				</div>
				`
		}
		label.innerHTML = label_html;
		knn_classes.innerHTML = knn_classes_html;
	}

	//update dataset table
	const update_dataset_table = (csv_data) =>{
		const [head,body] = dataset_table.children();
		let data = new Array(), columns = csv_data[0],
			obj = new Object(),key,value;
		for(let i=1;i<csv_data.length;i++){
			for(let j=0;j<columns.length;j++){
				obj[columns[j]] = csv_data[i][j] == undefined ? "":csv_data[i][j];
			}
			data.push(obj);
			obj = new Object();
		}
		console.log(csv_data)
		console.log(columns.map((value)=>{return {data:value}}))
		dataset_table.DataTable({
			data:data,
			columns:columns.map((value)=>{return {data:value}})
		});
	}
});

//to table html format
function to_table_html(array_data,tag_between){
	let html_out = `<tr>`;
	for(let i=0;i<array_data.length;i++){
		html_out += `<${tag_between}> ${array_data[i]} </${tag_between}>`;	
	}
	html_out += `</tr>`;
	return html_out;
}


