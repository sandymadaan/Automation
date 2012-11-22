function FilterTests(sel_val) {
	var testList = $('id_test');
	for (var count = testList.options.length-1; count >-1; count--){
		testList.options[count] = null;
	}
	testList.options[0] = new Option('Loading...', '-1', false, false);
	testList.disabled = true;

	var fieldList = $('id_field');
	var field_id = fieldList.options[fieldList.selectedIndex].value;
	if (field_id > 0) {
		new Ajax.Request('/test-by-field-id/' + field_id + '/', {
			method: 'get',
			onSuccess: function(transport){
				var response = transport.responseText || 'no response text';
				var kvpairs = response.split("\n");
				for (i=0; i<kvpairs.length - 1; i++) {
					m = kvpairs[i].split("\t");
					var option = new Option(m[1], m[0], false, false);
					testList.options[i] = option;
				}
				testList.disabled = false;
				if (sel_val > 0) {
					testList.value = sel_val;
				}
			},
			onFailure: function(){
				alert('An error occured trying to filter the test list.');
				testList.options[0] = new Option('Other', '0', false, false);
				testList.disabled = false;
			}
		});
	}
	else {
		testList.options[0] = new Option('Select Field', '-1', false, false);
		testList.disabled = true;
	}
}
