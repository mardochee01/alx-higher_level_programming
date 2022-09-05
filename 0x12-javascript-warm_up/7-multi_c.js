#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
