jQuery(function(){
    jQuery('#q').liveFilter('#fleet-list', {
        //useQuicksilver: true
    });
    jQuery('#form-fleet-filter').submit(function(e){
        e.stopPropagation();
        e.preventDefault();
        return false;
    });
});
