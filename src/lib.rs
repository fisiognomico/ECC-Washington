//! TODO add license
//! TODO add small explanation plus std libraries

#![no_std]
#![allow(unused_features)]
#![features(test)]

#[cfg(test)]
extern crate test;

#[macro_use]
extern crate arrayref;

#[cfg(feature="std")]
extern crate rand;

pub mod utils;

pub mod EC;

pub mod ElGamal;
pub mod DiffieHellman;

pub mod DSA;

pub mod main;
//!TODO add library
//!TODO add modules for curve and field
