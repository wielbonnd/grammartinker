(function(){
    var app = angular.module('grammartinker', ["ngTable"]);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

    app.controller("resultsController", controller);
    controller.$inject = ["NgTableParams"];

    function controller(NgTableParams) {
        var self = this;
        self.tableParams = new NgTableParams({}, {
            dataset: {{ responses|safe }}
        });
    }
}())
