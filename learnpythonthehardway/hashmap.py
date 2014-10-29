# -*- coding: utf-8 -*-

# new() function initializes one empty list of 265 sizes，ex:[[],[],[],...]
# hash_key() function generates a number to an index( bucket_id), one hash_key for one list of aMap
# get_bucket() function get the aMap[bucket_id] by hash_key (hash_key = bucket_id)
# get_slot() fuction make bucket = aMap[bucket_id], ex:[(k1,v1),(k2,v2),...]. if the given key exists,return i,k,v; otherwis return -1, key, default. 
# set() fuction use the return value of get_slot() to determine replace(bucket[i]=(key,value)) or add new one (bucket.append((key,value))
def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []	# aMap is a list within lists
	for i in range(0, num_buckets):
		aMap.append([])
	#print "new return: ", aMap
	return aMap	# aMap = [[],[]...[],[]]
	
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to an index for the aMap's buckets."""
	#print "hash_key returns: ", hash(key) % len(aMap)
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	#print "get_bucket returns: ", aMap[bucket_id]
	return aMap[bucket_id]	

	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key) # bucket等于aMap list中的一项，并且bucket自身也是一个list
	
	for i, kv in enumerate(bucket):	# bucket = [(k1,v1),(k2,v2),...],bucket中的每项包含多个参数
		k, v = kv	
		if key == k:
			return i, k, v	# ex1: i=0,k=k1,v=v1
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))
	print "i: ",i, "\tk: ",key, "\tvalue: ", value
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
def list(aMap):
	"""Prints our what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v