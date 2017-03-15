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

	console.log('start');
	$scope.selectedExercise = null;
	$scope.exerciseCount = null;
	$scope.submit = submit

	function submit(){
		if ($scope.selectedExercise === null || $scope.exerciseCount === null) {
			return null;
		}
		var requestUrl = '/api/insertIntoWorkoutTable/'+$scope.selectedExercise.id + '/'+ $scope.exerciseCount
		$http.get(requestUrl).then(function(){
			alert("Data inserted into DB");
		}, function(){
			alert("Error");
		});
	}

}
//});}
