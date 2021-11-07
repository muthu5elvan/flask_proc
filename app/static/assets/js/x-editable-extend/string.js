
(function ($) {
    "use strict";
    
    var String = function (options) {
        this.init('string', options, String.defaults);
    };

    //inherit from Abstract input
    $.fn.editableutils.inherit(String, $.fn.editabletypes.abstractinput);

    $.extend(String.prototype, {
        
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
            this.$input.val(value)
        },
        // set focus
        activate: function() {
            this.$input.focus();
        },

        // after edit the input
        // extract value from input
        input2value: function() { 
            return this.$input.val();
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

    String.defaults = $.extend({}, $.fn.editabletypes.abstractinput.defaults, {
        tpl: `<div class="editable-input">
                <input  class="form-control" type="text" />
            </div>`,
        inputclass: ''
    });

    $.fn.editabletypes.string = String;

}(window.jQuery));

