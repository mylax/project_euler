const funcs = require('./funcs.js');

var expect = require('chai').expect;

describe('#find_multiples()', function() {
    it('should work for a single number', function() {
        expect(funcs.find_multiples([3], 10)).to.have.members([3, 6, 9])
    });
    it('should work for multiple numbers', function() {
        expect(funcs.find_multiples([3, 4], 10)).to.have.members([3, 4, 6, 8, 9])
    });
    it('should not include the limit', function() {
        expect(funcs.find_multiples([3, 5], 10)).to.have.members([3, 5, 6, 9])
    });
});