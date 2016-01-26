(function(){
    var app = angular.module('grammartinker', []);

    app.config(function($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });


    app.directive('response', function() {
        return {
          restrict: 'E',
          scope: { isCorrect: '=', correctResponse: '=', answered: '=' },
          template:
            '<span class="glyphicon glyphicon-ok text-success form-control-feedback" ng-show="answered && isCorrect" ></span><span class="glyphicon glyphicon-remove text-danger form-control-feedback" ng-show="answered && !isCorrect" ></span><span class="text-danger help-inline" ng-show="answered && !isCorrect" >{$ correctResponse $}</span>'
        };
      })

    app.controller("Exercise", function($http) {
        var vm = this;
        var model = {};
        var verbs = [
            {infinitive: 'read',  simple_past: 'read', past_participle: 'read'},
            {infinitive: 'lay',  simple_past: 'laid', past_participle: 'laid'},
            {infinitive: 'lead',  simple_past: 'led', past_participle: 'led'}
        ];
        var responses = []

        vm.currentVerbIndex = 0;

        vm.reponse = {
           simple_past: '',
           simple_past_correct: false,
           past_participle: '',
           past_participle_correct: false
        }

        vm.checkClick = checkReponse;
        vm.nextVerbClick = nextVerb;
        vm.loading = true;

        // TODO: move http communication to service
        $http({
            method: 'GET',
            url: '{% url "verbs:random" %}'
        }).then(function successCallback(response) {
            verbs = response.data;
            vm.verbsAmount = verbs.length;
            vm.verb = verbs[vm.currentVerbIndex];
            vm.reponse.infinitive = vm.verb.infinitive;
            vm.loading = false;
        });

        function nextVerb() {
            responses.push(vm.response);

            //  save response to server
            $http.post(
                '{% url "responses:save-response" response_session.id %}',
                vm.reponse
            )
            vm.answered = false;
            vm.currentVerbIndex += 1;
            vm.verb = verbs[vm.currentVerbIndex];
            vm.reponse = {
                infinitive: vm.verb.infinitive,
                simple_past: '',
                simple_past_correct: false,
                past_participle: '',
                past_participle_correct: false
            }
        }

        function checkReponse() {
            vm.reponse.simple_past_correct = vm.reponse.simple_past.trim().toLowerCase() == vm.verb.simple_past;
            vm.reponse.past_participle_correct = vm.reponse.past_participle.trim().toLowerCase() == vm.verb.past_participle;
            vm.answered = true;
        }
    })


}())
