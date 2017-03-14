angular.module('whatthefit', []);

angular.module('whatthefit')
    .controller('workoutController', workoutController);

workoutController.$inject = ['$scope', '$http'];

function workoutController($scope, $http) {
    $scope.selectedExercise = null;

}
