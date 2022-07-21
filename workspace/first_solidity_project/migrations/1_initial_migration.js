const Migrations = artifacts.require("Migrations");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};

var HelloWorld = artifacts.require('HelloWorld');

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(HelloWorld);
};