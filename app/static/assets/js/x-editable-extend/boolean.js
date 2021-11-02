(function ($) {
    "use strict";
    
    var Boolean = function (options) {
        this.init('boolean', options, Boolean.defaults);
    };

    //inherit from Abstract input
    $.fn.editableutils.inherit(Boolean, $.fn.editabletypes.abstractinput);

    $.extend(Boolean.prototype, {
        
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
        },
        // assign value to input
        value2input: function(value) {
            if(!value) {
                return;
            }
            if(value == "true"){
                this.$input.attr("checked",true);
            }
            else{
                this.$input.attr("checked",false);
            }
        },
        // set focus
        activate: function() {
            this.$input.focus();
        },

        // after edit the input
        // extract value from input
        input2value: function() { 
            return this.$input[0].checked;
        },
        // change type extracted value
        value2str: function(value) {
            try{
                return value.toString();
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
        autosubmit: function() {
            this.$input.keydown(function (e) {
                if (e.which === 13) {
                    $(this).closest('form').submit();
                }
            });
        }       
    });

    Boolean.defaults = $.extend({}, $.fn.editabletypes.abstractinput.defaults, {
        tpl: `<div class="editable-input">
                <input type="checkbox" id="switch3" switch="bool" checked/>
                    <label for="switch3" data-on-label="Yes" data-off-label="No"></label>
            </div>`,
        inputclass: ''
    });

    $.fn.editabletypes.boolean = Boolean;

}(window.jQuery));
