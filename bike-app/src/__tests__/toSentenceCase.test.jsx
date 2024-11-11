import toSentenceCase from "../toSentenceCase";
import { describe, expect, it } from 'vitest';

console.log('Running a test...');

describe("Conduct tests using the toSentenceCase function...", () => {
   it("The to sentence case of of hello and world!", () => {
     expect(toSentenceCase('hello world!')).toBe('Hello World!');
  });
});