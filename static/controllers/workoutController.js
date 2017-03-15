angular.module('whatthefit', []);

angular.module('whatthefit')
    .config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('{a');
        $interpolateProvider.endSymbol('a}');
    }]);

angular.module('whatthefit')
    .controller('workoutController', workoutController);

workoutController.$inject = ['$scope', '$http'];

function workoutController($scope, $http) {
    //angular.element(document).ready(function(){
  //console.log('test');
	//$scope.test = 'test';
	console.log('start');
	$scope.selectedExercise = null;
       setInterval(function(){
	console.log($scope.selectedExercise);
	},1000);
}
//});}
