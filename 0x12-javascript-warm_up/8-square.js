#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  const sizeSquare = parseInt(process.argv[2]);
  for (let i = 0; i < sizeSquare; i++) {
    console.log('X'.repeat(sizeSquare));
  }
} else {
  console.log('Missing size');
}
