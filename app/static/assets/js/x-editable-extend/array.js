
(function ($) {
    "use strict";
    
    var Array = function (options) {
        this.init('object', options, Array.defaults);
    };

    //inherit from Abstract input
    $.fn.editableutils.inherit(Array, $.fn.editabletypes.abstractinput);

    $.extend(Array.prototype, {
        str2value: function(str) {
            try{
                return str.toString();
            }catch (e){
                console.log("[E]",e)
                return ""
            }
        },                
        // input element render
        render: function() {
            this.$input = this.$tpl.find("input");
            this.$input.tagsinput();
        },
        // assign value to input
        value2input: function(value) {
            this.$tpl.find("div.bootstrap-tagsinput").addClass("bg-light")
            this.$tpl.find("div.bootstrap-tagsinput").sortable({
                update: function(event, ui) {
                    try{
                        var input_array=[]
                        $.each(this.$tpl.find("div.bootstrap-tagsinput").find("span"),function(index,spanElement){
                            if ($(spanElement).text() !=""){
                                input_array.push($(spanElement).text())
                            }
                        })
                        this.$input.val(input_array)
                    }catch(e){}
                }
            });
            this.$tpl.find("div.bootstrap-tagsinput").find("input").attr("size","1")
            this.$input.tagsinput("add",value)
        },
        // set focus
        activate: function() {
            this.$input.tagsinput('focus');
        },

        // after edit the input
        // extract value from input
        input2value: function() { 
            var input_array=[]
            $.each(this.$tpl.find("div.bootstrap-tagsinput").find("span"),function(index,spanElement){
                if ($(spanElement).text() !=""){
                    input_array.push($(spanElement).text())
                }
            })
            return input_array;
        },
        // change type extracted value
        value2str: function(value) {
            this.$input.val(value)
            //console.log(value)
            try{
                return value;
            }catch(e){
                
                console.log("[E]",e,this.$input[0])
                return "";
            }
        },
        // change data in the main
        value2html: function(value, element) {  
            $(element).html(value.toString()); 
        },
        html2value: function(html) {   
            return null;  
        },
        autosubmit: function(value) {
            this.$input.keydown(function (e) {
                if (e.which === 13) {
                    $(this).closest('form').submit();
                }
            });
        }       
    });

    Array.defaults = $.extend({}, $.fn.editabletypes.abstractinput.defaults, {
        tpl: `
        <div class="editable-input">
        <input class="form-control" type="text" data-role="tagsinput"  />
            </div>
            `,
        inputclass: ''
    });

    $.fn.editabletypes.object = Array;

}(window.jQuery));